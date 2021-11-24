import sqlite3
from typing import List

# общий класс для работы с б
# д
class DataBase:
    def __init__(self):
        # подключение бд
        self.connect = sqlite3.connect('db/messenger.db')

    # метод создания запроса для получения значений из бд
    def get_response(self, table, **kwargs) -> List[tuple]:
        self.cursor = self.connect.cursor()
        request = f'''select * from {table}'''
        if kwargs:
            request += ' WHERE ' + ' AND '.join([f'{k} == {v}' if
                                                 type(v).__name__ == 'int'
                                                 else f'{k} == "{v}"' for
                                                 k, v in kwargs.items()])
        return self.cursor.execute(request).fetchall()

    # метод создания запроса для занесения значений в бд
    def post_response(self, table, **kwargs):
        self.cursor = self.connect.cursor()
        request = f'''insert into {table}'''
        if kwargs:
            request += '(' + ', '.join([k for k in kwargs.keys()]) + ')' + \
                       'values' + '(' + ', '.join(
                [f'{v}' if type(v).__name__ == 'int' else f'"{v}"' for v in
                 kwargs.values()]) + ')'
        self.cursor.execute(request)
        self.connect.commit()

    # метод создания запроса для изменений значений в бд
    def put_response(self, table, update: dict, where: dict):
        self.cursor = self.connect.cursor()
        request = f'''update {table}'''
        if update and where:
            request += ' set ' + ", ".join(
                [f"{k}={v}" if type(v).__name__ == 'int' else f'{k}="{v}"' for
                 k, v in update.items()]) + ' where ' + ' and '.join(
                [f"{k}={v}" if type(v).__name__ == 'int' else f'{k}="{v}"' for
                 k, v in where.items()])
        print(request)
        self.cursor.execute(request)
        self.connect.commit()
