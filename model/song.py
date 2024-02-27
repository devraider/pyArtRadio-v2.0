from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Song(SQLModel, table=True):
    __tablename__ = "radio_songs"
    id: Optional[int] = Field(default=None, primary_key=True)
    radio_id: Optional[int] = Field(default=None, foreign_key="radio.id")
    singer: str
    name: str
    raw_song: str
    youtube_id: str
    likes: Optional[int] = Field(default=0)
    dislikes: Optional[int] = Field(default=0)
    date_stream_played: datetime = Field(default_factory=lambda: datetime.now())
    date_inserted: datetime = Field(default_factory=lambda: datetime.now())

