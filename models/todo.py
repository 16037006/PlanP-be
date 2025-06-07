from datetime import datetime, date
from typing import Optional

from sqlmodel import SQLModel, Field


class TodoBase(SQLModel):
    title: str
    description: Optional[str] = Field(None, nullable=True)
    plan_date: date  # 예정 날짜
    start_time: Optional[datetime] = Field(None, nullable=True)  # 예정 시작 시간
    end_time: Optional[datetime] = Field(None, nullable=True)  # 예정 종료 시간
    location: Optional[str] = Field(None, nullable=True)


class Todo(TodoBase, table=True):
    id: int | None = Field(None, primary_key=True)
