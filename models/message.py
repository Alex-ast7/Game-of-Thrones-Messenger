import datetime

from pydantic import BaseModel


# класс для установки типов в таблице бд
class Message(BaseModel):
    id: int
    time: datetime.datetime
    text: str
    name: str
    chat: str
