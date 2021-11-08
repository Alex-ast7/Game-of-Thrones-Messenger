import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    time: datetime.datetime
    text: str
    name: str
    chat: str