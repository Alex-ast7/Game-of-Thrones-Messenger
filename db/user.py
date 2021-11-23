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

    def post(self, user):
        self.db.post_response(table='User', name=user)