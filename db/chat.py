from db.db import DataBase
from models.chat import Chat


# класс для работы с таблицей в бд
class ChatDB:
    def __init__(self, db):
        self.db = db

    # метод для получения значений из бд
    def get(self, **kwargs):
        response = []
        for elem in self.db.get_response(table='Chat', **kwargs):
            response.append(Chat(id=elem[0], title=elem[1]))
        return response
