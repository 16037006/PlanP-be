from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlmodel import Session

from database import get_session
from models.todo import Todo, TodoBase
from services.todo import create_todo, get_todo

router = APIRouter()


@router.get("/get/{todo_id}")
async def get(
        session: Annotated[Session, Depends(get_session)],
        todo_id: int = Path(ge=0)
):
    todo = get_todo(session, todo_id=todo_id)

    return todo


@router.post("/create")
async def create(
        session: Annotated[Session, Depends(get_session)],
        todo: TodoBase,
):
    todo = create_todo(session, todo)

    return todo
