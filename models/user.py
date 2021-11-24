from pydantic import BaseModel


# класс для установки типов в таблице бд
class User(BaseModel):
    id: int
    name: str
