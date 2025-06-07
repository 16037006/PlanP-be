from fastapi import FastAPI

from database import create_db_and_tables
from routers import todo

create_db_and_tables()
app = FastAPI()

# 라우터 등록
app.include_router(todo.router)
