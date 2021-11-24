from models.user import User


# класс для работы с таблицей в бд
class UserDB:
    def __init__(self, db):
        self.db = db

    # метод занесения аргументов в запрос для общего класса бд: получение
    # записей
    def get(self, **kwargs):
        response = []
        for elem in self.db.get_response(table='User', **kwargs):
            response.append(User(id=elem[0], name=elem[1]))
        return response

    # метод занесения аргументов в запрос для общего класса бд: изменение
    # записей
    def post(self, user):
        self.db.post_response(table='User', name=user)