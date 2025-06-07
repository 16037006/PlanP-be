from datetime import date
from typing import List

from sqlmodel import Session, select

from exceptions.todo import TodoNotFoundException
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
        emothion=todo_base.emothion,
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


def get_todos_by_plan_date(db: Session, plan_date: date) -> List[Todo]:
    todos = db.exec(
        select(Todo).where(Todo.plan_date == plan_date).order_by(Todo.start_time)
    ).all()
    return todos


def get_todos_by_title(db: Session, title: str) -> List[Todo]:
    # TODO: 제목으로 찾기 구현
    pass


def get_todos_weekly(db: Session, title: str) -> List[Todo]:
    # TODO: 주간 일정 불러오기 구현
    # TODO: 불러온 일정 갯수 카운트 구현
    pass


def remove_todo(db: Session, todo_id: int) -> bool:
    # TODO: 일정삭제 구현
    return True


def modify_todo(db: Session, todo_id: int, todo_base: TodoBase) -> Todo:
    # 수정할 todo 있는지 확인
    if not db.get(Todo, todo_id):
        raise TodoNotFoundException(status_code=404, detail=f"{todo_id=} 해당하는 계획이 없습니다. ")

    # Update 수행
    todo = todo_base.model_dump(exclude_unset=True)
    todo.sqlmodel_update(todo_base)

    # DB 에 저장
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo
