import datetime

from db.chat import ChatDB
from db.db import DataBase
from db.user import UserDB
from models.message import Message


class MessageDB:
    def __init__(self, db: DataBase):
        self.db = db

    def get(self, **kwargs):
        response = []
        for elem in self.db.get_response(table='Messages', **kwargs):
            print(elem)
            response.append(Message(table='', name=UserDB(self.db).get(id=int(elem[1]))[0].name,
                                    time=datetime.datetime.strptime(elem[3], '%H:%M:%S %d-%m-%Y'), text=elem[2], id=elem[0],
                                    chat=ChatDB(self.db).get(id=int(elem[4]))[0].title))
        return response

    def post(self, message: Message):
        self.db.post_response(table='Messages', user=int(UserDB(self.db).get(name=message.name)[0].id),
                           time=datetime.datetime.strftime(message.time, '%H:%M:%S %d-%m-%Y'),
                           text=message.text,
                           chat=ChatDB(self.db).get(title=message.chat)[0].id)
