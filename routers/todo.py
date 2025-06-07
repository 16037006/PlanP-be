from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from sqlmodel import Session

from database import get_session
from models.todo import Todo, TodoBase
from services.todo import(
    create_todo,
    get_todo,
    get_todos_by_plan_date,
    get_todos_by_title,
    get_todos_between_date,
    get_todos_this_weekly,
    get_todos_by_description,
    remove_todo,
    modify_todo
)

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


@router.get("/get-by-plan-date/")
async def get_by_plan_date(
        session: Annotated[Session, Depends(get_session)],
        plan_date: date
):
    todos = get_todos_by_plan_date(session, plan_date)
    return todos


@router.get("/get-by-title/")
async def get_by_title(
        session: Annotated[Session, Depends(get_session)],
        title: str = Query(...)
):
    todos = get_todos_by_title(session, title)
    return todos


@router.get("/get-between-date/")
async def get_between_date(
        session: Annotated[Session, Depends(get_session)],
        start_date: date,
        end_date: date
):
    todos = get_todos_between_date(session, start_date, end_date)
    return todos


@router.get("/get-this-week/")
async def get_this_week(
        session: Annotated[Session, Depends(get_session)],
        today_date: date = Query(default=date.today())
):
    todos = get_todos_this_weekly(session, today_date)
    return todos


@router.get("/get-by-description/")
async def get_by_description(
        session: Annotated[Session, Depends(get_session)],
        description: str = Query(...)
):
    todos = get_todos_by_description(session, description)
    return todos


@router.delete("/delete/{todo_id}")
async def delete(
        session: Annotated[Session, Depends(get_session)],
        todo_id: int = Path(ge=0)
):
    result = remove_todo(session, todo_id)
    return {"success": result}


@router.put("/modify/{todo_id}")
async def modify(
        session: Annotated[Session, Depends(get_session)],
        todo_id: int = Path(ge=0),
        todo: TodoBase = ...
):
    updated = modify_todo(session, todo_id, todo)
    return updated