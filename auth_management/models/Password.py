from datetime import datetime

from sqlmodel import SQLModel, Field


class Password(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    password: str
    hashed_special_key: str
    is_enabled: bool
    created_at: datetime
    updated_at: datetime
