from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from database import init_db
from config.setting import settings
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    # await init_db()
    yield
app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix=settings.API_V1_STR)
