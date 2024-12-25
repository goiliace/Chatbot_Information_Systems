from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config.setting import settings

async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True,
    # statement_cache_size=0
)


async def init_db():
    async with async_engine.begin() as conn:
        # from ..users.models import User
        # from ..matchs.models import Match
        from model.model import User, Conversation, Message
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=True,
    )

    async with async_session() as session:
        yield session
