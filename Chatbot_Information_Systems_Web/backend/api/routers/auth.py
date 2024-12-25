from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from security import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token, get_current_active_user, create_account
from model.model import User
from typing import Optional
from model.model import User, Status  # Ensure these are imported

from datetime import datetime, timedelta
from sqlmodel.ext.asyncio.session import AsyncSession
from http import HTTPStatus
from service.auth import UserService
from database import get_session
router = APIRouter()

@router.post("/all")
async def get_all(
    session: AsyncSession = Depends(get_session)
):
    user_service = UserService(session)
    return await user_service.get_all_users()
# FastAPI route for token generation (login)

@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Example route that requires authentication
@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.post("/register")
async def register(
    email: str,
    password: str,
    name: Optional[str] = None,
    session: AsyncSession = Depends(get_session),
):
    new_user = await create_account(session, email, password, name)
    return {"msg": "User created successfully", "user_id": new_user.id}
