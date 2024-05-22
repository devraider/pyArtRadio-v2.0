from typing import Optional

from sqlmodel import SQLModel, Field


class Radio(SQLModel, table=True):
    __tablename__ = "radio"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str
    url: str
    img: str
    description: str
    contact: str
