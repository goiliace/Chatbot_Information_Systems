from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from model.model import Message
from typing import List, Optional, Sequence
from uuid import UUID
class HistoryService:
    def __init__(self, session: AsyncSession, thread_id: UUID):
        self.session = session
        self.thread_id = thread_id
    
    async def add_message(self, message: Message):
        try:
            self.session.add(message)       
            await self.session.commit()
            await self.session.refresh(message)
            return message
        except Exception as e:
            raise e

    async def add_messages(self, messages: Sequence[Message]):
        self.session.add_all(messages)       
        await self.session.commit()
        await self.session.refresh(messages)
        return messages
    
    async def get_messages(self, offset: Optional[int] = None,limit: Optional[int] = None) -> List[Message]:
        statement = select(Message).where(Message.conversation_id == self.thread_id).order_by(Message.create_at).offset(offset).limit(limit)
        result = await self.session.exec(statement)
        messages = result.all()
        return messages       
              
    async def update_message(self,message_id: UUID, content: str):
        statement = select(Message).where(Message.id == message_id)
        result = await self.session.exec(statement)
        message = result.one()
        message.content = content
        await self.session.commit()
        return message
    
    async def delete_message(self, message_id: UUID):
        statement = select(Message).where(Message.id == message_id)
        result = await self.session.exec(statement)
        message = result.one()
        self.session.delete(message)
        await self.session.commit()
        return message