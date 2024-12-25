from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID, ENUM, TIMESTAMP
from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel
import uuid

# Enum types
class RoleMessage(str, Enum):
    human = "human"
    assistance = "assistance"
    system = "system"

class RoleUser(str, Enum):
    admin = "admin"
    employee = "employee"
    user = "user"

class Status(str, Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"

class MessageReactType(str, Enum):
    like = "like"
    dislike = "dislike"
    noaction = "noaction"

# Models
class User(SQLModel, table=True):
    __tablename__ = "user"
    id: uuid.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("uuid_generate_v4()"),
        )
    )
    email: str = Field(
        sa_column=Column(String, nullable=False, unique=True, index=True)
    )
    name: Optional[str] = None
    status: Status = Field(
        sa_column=Column(ENUM(Status, name="status"), nullable=False, server_default=text("'active'"))
    )
    role: RoleUser = Field(
        sa_column=Column(ENUM(RoleUser, name="roleuser"), nullable=False, server_default=text("'user'"))
    )
    hashed_password: str = Field(sa_column=Column(String, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
        )
    )
    photo_url: Optional[str] = Field(sa_column=Column(String))
    
class UserResponse(SQLModel):
    id: uuid.UUID
    email: str
    name: Optional[str] = None
    status: Status
    role: RoleUser
    created_at: datetime
    photo_url: Optional[str] = None

class Conversation(SQLModel, table=True):
    __tablename__ = "conversation"
    id: uuid.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("uuid_generate_v4()"),
        )
    )
    name: str = Field(sa_column=Column(String, nullable=False))
    is_active: bool = Field(sa_column=Column(Boolean, nullable=False, default=True))
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
        )
    )
    create_by: Optional[uuid.UUID] = Field(sa_column=Column(UUID(as_uuid=True)))


class BaseMessage(SQLModel):
    id: Optional[uuid.UUID] = Field(sa_column=Column(UUID(as_uuid=True)))
    content:  Optional[str] = Field(default=None)
    role:  RoleMessage = Field(
        sa_column=Column(
            ENUM(RoleMessage, name="rolemessage"), nullable=False
        )
    )
    conversation_id: Optional[uuid.UUID] = Field(sa_column=Column(UUID(as_uuid=True)))
    
class Message(SQLModel, table=True):
    __tablename__ = "message"
    id: uuid.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("uuid_generate_v4()"),
        )
    )
    content: Optional[str] = Field(default=None)
    url: Optional[str] = Field(default=None)
    role: Optional[str] = Field(default=None)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
        )
    )
    conversation_id: Optional[uuid.UUID] = Field(sa_column=Column(UUID(as_uuid=True)))
    user_react: MessageReactType = Field(
        sa_column=Column(
            ENUM(MessageReactType, name="messagereacttype_enum"),
            nullable=False,
            server_default=text("'noaction'"),
        )
    )
