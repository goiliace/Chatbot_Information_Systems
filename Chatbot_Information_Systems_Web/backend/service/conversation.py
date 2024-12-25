from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from model.model import Conversation
from typing import List, Optional, Sequence
from uuid import UUID

class ConversationService:
    def __init__(self, session: AsyncSession, user_id: UUID):
        self.session = session
        self.user_id = user_id
    
    async def add_conversation(self, conversation: Conversation):
        print(conversation)
        self.session.add(conversation)
        await self.session.commit()
        await self.session.refresh(conversation)
        return conversation
    
    async def get_conversation_by_id(self, conversation_id: UUID):
        statement = select(Conversation).where(Conversation.id == conversation_id)
        result = await self.session.exec(statement)
        conversation = result.one()
        return conversation
    async def get_conversation(self, offset: Optional[int] = None,limit: Optional[int] = None) -> List[Conversation]:
        statement = select(Conversation).where(Conversation.create_by == self.user_id).where(Conversation.is_active == True).order_by(desc(Conversation.create_at)).offset(offset).limit(limit)
        result = await self.session.exec(statement)
        conversations = result.all()
        return conversations
    
    async def update_conversation(self, conversation_id: UUID, name: str):
        statement = select(Conversation).where(Conversation.id == conversation_id)
        result = await self.session.exec(statement)
        conversation = result.one()
        conversation.name = name
        await self.session.commit()
        return conversation

    async def delete_conversation(self, conversation_id: UUID):
        statement = select(Conversation).where(Conversation.id == conversation_id)
        result = await self.session.exec(statement)
        conversation = result.one()
        self.session.delete(conversation)
        await self.session.commit()
        return conversation