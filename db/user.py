from db.db import DataBase
from models.user import User


class UserDB:
    def __init__(self, db):
        self.db = db

    def get(self, **kwargs):
        response = []
        for elem in self.db.get_response(table='User', **kwargs):
            response.append(User(id=elem[0], name=elem[1]))
        return response
    #
    # def post(self, user):
    #     self.db.post_response(table='User', user=int(UserDB(self.db).get(name=message.name)[0].id),
    #                        time=datetime.datetime.strftime(message.time, '%H:%M:%S %d-%m-%Y'),
    #                        text=message.text,
    #                        chat=ChatDB(self.db).get(title=message.chat)[0].id)