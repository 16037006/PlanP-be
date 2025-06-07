from datetime import datetime, date
from typing import Optional

from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True):
    id: int | None = Field(None, primary_key=True)
    plan_date: date  # 예정 날짜
    start_time: datetime | None  # 예정 시작 시간
    end_time: datetime | None  # 예정 종료 시간
    title: str
    description: Optional[str]
    location: Optional[str]