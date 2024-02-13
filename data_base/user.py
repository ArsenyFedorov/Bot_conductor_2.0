import sqlite3
from data_base.data_base import DataBase
from aiogram.types import Message


class User(DataBase):
    def __init__(self, data: int):
        self.user = self.load(tg_id=data)

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS user
                    (tg_id INTEGER, name TEXT)'''
        User.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM user WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        user = self.execute(sql, parameters, fetchone=True)
        return user

    def create(self, tg_id: int, name: str):
        sql = """SELECT * FROM user WHERE tg_id=?"""
        data = self.execute(sql, (tg_id,), fetchone=True)
        if data:
            print("Такой пользователь уже есть ) ")
        else:
            sql = """INSERT INTO user(tg_id,name) VALUES (?,?)"""
            self.execute(sql, (tg_id, name), commit=True)
