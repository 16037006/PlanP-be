from datetime import date, datetime
from typing import Optional

from sqlmodel import Session

from exceptions.todo import TodoException, TodoNotFoundException
from models.todo import Todo, TodoBase


def create_todo(
        db: Session,
        todo_base: TodoBase
) -> Todo:
    todo = Todo(
        id=None,
        title=todo_base.title,
        description=todo_base.description,
        plan_date=todo_base.plan_date,
        start_time=todo_base.start_time,
        end_time=todo_base.end_time,
        location=todo_base.location,
    )

    # DB 에 저장
    db.add(todo)
    db.commit()
    db.refresh(todo)

    # 반환
    return todo

def get_todo(db: Session, todo_id: int) -> Todo:
    todo = db.get(Todo, todo_id)
    if not todo:
        raise TodoNotFoundException(status_code=404, detail=f"{todo_id=} 해당하는 계획이 없습니다. ")

    return todo