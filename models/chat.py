from pydantic import BaseModel


# класс для установки типов в таблице бд
class Chat(BaseModel):
    id: int
    title: str
