from datetime import datetime, timedelta
from typing import Optional
from database import get_session
import uuid

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from model.model import User, Status, UserResponse  # Your SQLModel User model
from service.auth import UserService  # The UserService class you defined

# Secret key for JWT
SECRET_KEY = "354657utjyhdgrsfeawdq2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")

# Password hashing functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# JWT token creation
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Authenticate user credentials
async def authenticate_user(session: AsyncSession, email: str, password: str) -> Optional[User]:
    user_service = UserService(session)
    user = await user_service.get_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Dependency to get the current user from the token
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user_service = UserService(session)
    user = await user_service.get_user_by_id(user_id)
    if user is None:
        raise credentials_exception
    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        status=user.status,
        role=user.role,
        created_at=user.created_at,
        photo_url=user.photo_url
    )

# Dependency to get the current active user
async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.status != Status.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Function to create a new user (account creation)
async def create_account(
    session: AsyncSession,
    email: str,
    password: str,
    name: Optional[str] = None,
) -> User:
    user_service = UserService(session)
    existing_user = await user_service.get_user_by_email(email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(password)
    new_user = User(
        id=uuid.uuid4(),
        email=email,
        hashed_password=hashed_password,
        name=name,
        status=Status.active,
        role="user",
        created_at=datetime.utcnow(),
    )
    await user_service.create_user(new_user)
    return new_user

