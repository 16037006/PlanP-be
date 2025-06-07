from datetime import date, timedelta
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
    todos = db.exec(
        select(Todo).where(Todo.title == title).order_by(Todo.start_time))
    if not todos:
        raise TodoNotFoundException(status_code=404, detail=f"{title=}에 해당하는 계획이 없습니다. ")

    return todos


def get_todos_between_date(db: Session, start_date: date, end_date: date) -> List[Todo]:
    todos = db.exec(
        select(Todo)
        .where(Todo.plan_date >= start_date, Todo.plan_date <= end_date)
        .order_by(Todo.start_time)
    ).all()
    return todos


def get_todos_this_weekly(db: Session, today_date: date) -> List[Todo]:
    weekday = today_date.isoweekday() % 7
    # 일요일 기준 이번주의 시작일을 선언
    start_of_week = today_date - timedelta(days=weekday)
    # 이번 주의 마지막 토요일을 선언
    end_of_week = start_of_week + timedelta(days=6)

    return get_todos_between_date(db, start_of_week, end_of_week)


def remove_todo(db: Session, todo_id: int) -> bool:
    todo = db.get(Todo, todo_id)
    if not todo:
        raise TodoNotFoundException(status_code=404, detail=f"{todo_id=} 해당하는 계획이 없습니다. ")

    db.delete(todo)
    db.commit()
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


def get_todos_by_description(db: Session, description: str) -> List[Todo]:
    # description에 작성한 내용 중 일치하는 단어가 있으면 조회 (LIKE '%단어%')
    todos = db.exec(
        select(Todo)
        .where(Todo.description.like(f"%{description}%"))
        .order_by(Todo.start_time)
    ).all()

    if not todos:
        raise TodoNotFoundException(
            status_code=404,
            detail=f"{description=}이 포함된 계획이 없습니다."
        )

    return todos