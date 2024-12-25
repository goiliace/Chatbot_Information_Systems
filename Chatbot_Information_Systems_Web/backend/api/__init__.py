from fastapi import APIRouter
from api.routers import auth
from api.routers import converstation

router = APIRouter()

router.include_router(converstation.router, prefix='/conversation', tags=['conversation'])
router.include_router(auth.router, prefix='/auth', tags=['auth'])