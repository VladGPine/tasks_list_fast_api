from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('db is cleared')
    await create_tables()
    print('db is created')
    yield
    print('turn off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
