from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from model.model import User

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
    async def get_all_users(self):
        statement = select(User)#.where(User.is_active == True)
        result = await self.session.exec(statement)
        return result.all()
    
    async def create_user(self, user: User):
        print(user)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_user_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        result = await self.session.exec(statement)
        return result.first()
    async def get_user_by_id(self, user_id: str):
        statement = select(User).where(User.id == user_id)
        result = await self.session.exec(statement)
        return result.first()
    
    async def update_user(self, user: User):
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def delete_user(self, user: User):
        await self.session.delete(user)
        await self.session.commit()
        return user
    