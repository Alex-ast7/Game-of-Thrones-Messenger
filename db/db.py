import sqlite3
from typing import List


class DataBase:
    def __init__(self):
        self.connect = sqlite3.connect('db/messenger.db')

    def get_response(self, table, **kwargs) -> List[tuple]:
        self.cursor = self.connect.cursor()
        request = f'''select * from {table}'''
        if kwargs:
            request += ' WHERE ' + ' AND '.join([f'{k} == {v}' if
                                                 type(v).__name__ == 'int'
                                                 else f'{k} == "{v}"' for
                                                 k, v in kwargs.items()])
        return self.cursor.execute(request).fetchall()

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
