from fastapi import APIRouter, Depends
# http exception
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse
from llms.workflow import pipeline

from langchain_core.messages import AnyMessage, BaseMessage
from llms.rag import generator_norag_pipeline

# from model.converstation import ChatRequest, CreateThreadRequest
from sqlmodel.ext.asyncio.session import AsyncSession
from database import get_session
from service.history import HistoryService
from service.conversation import ConversationService
from uuid import uuid4, UUID
from security import get_current_active_user
from model.model import User
from model.model import Message, Conversation
from pydantic import BaseModel
from llms.router import gen_route_and_rewrite, gen_title
from llms.llm import generator_mis_pipeline
from typing import List
from uuid import UUID
from datetime import datetime

router = APIRouter()


@router.post("/create")
async def create_conversation(
    current_user: User = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session)
):
    conversation_service = ConversationService(session, current_user.id)
    conversation_id = uuid4()
    conversation = Conversation(
        id=conversation_id,
        name="New chat",
        create_by=current_user.id
    )
    try:
        await conversation_service.add_conversation(conversation)
        return conversation_id
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating conversation")
@router.put("/update")
async def update_conversation(
    conversation_id: UUID,
    name: str,
    current_user: User = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session)
):
    conversation_service = ConversationService(session, current_user.id)
    try:
        await conversation_service.update_conversation(conversation_id, name)
        return  await conversation_service.update_conversation(conversation_id, name)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error updating conversation")

@router.get("/all")
async def get_all_conversation(
    offset: int = 0,
    limit: int = 20,
    current_user: User = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session)
):
    user_id = current_user.id
    conversation_service = ConversationService(session, user_id=user_id)
    conversation = await conversation_service.get_conversation(
        offset=offset,
        limit=limit
    )
    return conversation
    
    
    
@router.get("/history")
async def get_history(
    conversation_id: UUID,
    offset: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session)
):
    history_service = HistoryService(session, conversation_id)
    history = await history_service.get_messages(
        offset=offset,
        limit=limit
    )
    return history

@router.post("/history")
async def add_history(
    thread_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    history_service = HistoryService(session, thread_id)
    history = await history_service.get_messages()
    return history          
    
async def generation(question:str, 
                     history: List[AnyMessage],
                     message: Message,
                     history_service: HistoryService,
                     is_update_conversation_name: bool = False,
                     conversation_service = None,
                     conversation_id = None
                     ):
    async for chunk in generator_mis_pipeline.astream({"question": question, "history": history}):
        message.content += chunk.content
        yield chunk.content
    await history_service.update_message(message.id, message.content)
    if is_update_conversation_name:
        h = [
            {"role": "human", "content": question},
            {"role": "ai", "content": message.content}
        ]
        title = await gen_title({"history": h})
        await conversation_service.update_conversation(conversation_id, title['title'])   
async def generation_rag(question:str, 
                     history: List[AnyMessage],
                     message: Message,
                     history_service: HistoryService,
                     is_update_conversation_name: bool = False,
                     conversation_service = None,
                     conversation_id = None
                     ):
    result = await pipeline.ainvoke({"question": question, "history": history})
    async for event in result:
        if event["event"] == "on_chat_model_stream":
            m: BaseMessage = event["data"]["chunk"]
            content = m.content
            message.content += content
            await history_service.update_message(message.id, message.content)
            yield content
    if is_update_conversation_name:
        title = await gen_title({"history": [
            {"role": "human", "content": question},
            {"role": "ai", "content": message.content}
        ]})
        await conversation_service.update_conversation(conversation_id, title['title'])
class ChatRequest(BaseModel):
    question: str
    conversation_id: str
    is_rag: bool
async def norag_generation(question:str, 
                     history: List[AnyMessage],
                     message: Message,
                     history_service: HistoryService,
                     is_update_conversation_name: bool = False,
                     conversation_service = None,
                     conversation_id = None
                     ):
    async for chunk in generator_norag_pipeline.astream({"question": question, "history": history}):
        message.content += chunk.content
        yield chunk.content
    await history_service.update_message(message.id, message.content)
    if is_update_conversation_name:
        h = [
            {"role": "human", "content": question},
            {"role": "ai", "content": message.content}
        ]
        title = await gen_title({"history": h})
        await conversation_service.update_conversation(conversation_id, title['title'])
def message_to_dict(message: Message) -> dict:
    return {
        "id": str(message.id),
        "content": message.content,
        "role": message.role,
        "conversation_id": str(message.conversation_id) if message.conversation_id else None,
        "create_at": message.create_at.isoformat() if isinstance(message.create_at, datetime) else None,
    }
@router.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session)
):
    question = request.question
    history_service = HistoryService(session, request.conversation_id)
    messages = await history_service.get_messages(
        offset=0,
        limit=4
    )

    history = [message_to_dict(message) for message in messages if message.role != "system"]
    conversation_service = ConversationService(session, current_user.id)
    conversation = await conversation_service.get_conversation_by_id(request.conversation_id)
    is_update_conversation_name = False
    if len(history) == 0 or conversation.name == "New chat":
        is_update_conversation_name = True
    await history_service.add_message(Message(
        id=uuid4(),
        content=question,
        role="human",
        conversation_id=request.conversation_id
    ))
    
    message = Message(
        id=uuid4(),
        content="",
        role="ai",
        conversation_id=request.conversation_id
    )
    await history_service.add_message(message)
    if not request.is_rag:
        if is_update_conversation_name:
            return StreamingResponse(generation(question, history, message, history_service, is_update_conversation_name=is_update_conversation_name,
            conversation_service=conversation_service,
            conversation_id=request.conversation_id
            ), media_type="text/event-stream")
        else:
            return StreamingResponse(generation(question, history, message, history_service), media_type="text/event-stream")
    else:
        router = await gen_route_and_rewrite({"question": question,  "history": history})
        if router["router"] == "vectorstore":
            if is_update_conversation_name:
                return StreamingResponse(generation_rag(question, history, message, history_service, is_update_conversation_name=is_update_conversation_name,
                conversation_service=conversation_service,
                conversation_id=request.conversation_id
                ), media_type="text/event-stream")
            else:
                return StreamingResponse(generation_rag(question, history, message, history_service), media_type="text/event-stream")
        else:
            if is_update_conversation_name:
                return StreamingResponse(norag_generation(question, history, message, history_service, is_update_conversation_name=is_update_conversation_name,
                conversation_service=conversation_service,
                conversation_id=request.conversation_id
                ), media_type="text/event-stream")
            else:
                return StreamingResponse(norag_generation(question, history, message, history_service), media_type="text/event-stream")
