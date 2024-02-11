import sqlite3
from data_base.data_base import DataBase
from aiogram.types import Message


class Record(DataBase):

    def __init__(self, data):
        if isinstance(data, Message):
            self.tg_id = data.from_user.id
            self.name = data.from_user.first_name
            self.datetime = None
            self.status = "Не записан"
            self.create()
        if isinstance(data, int):
            self.tg_id = data
        user = self.load(tg_id=self.tg_id)
        self.tg_id, self.name, self.id_work, self.datetime, self.status = user

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS sport
                                 (tg_id INTEGER, name TEXT,
                                 id_work INTEGER PRIMARY KEY AUTOINCREMENT,
                                 datetime DATETIME, status TEXT)'''
        User.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM sport WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        user = self.execute(sql, parameters, fetchone=True)
        return user

    def save(self):
        sql = """UPDATE sport SET """
        sql, parameters = self.extract_kwargs(sql, self.__dict__, _and=False)
        sql = sql + f" WHERE tg_id={self.tg_id}"
        self.execute(sql, parameters, commit=True)

    def create(self):
        sql = """SELECT * FROM sport WHERE tg_id=?"""
        data = self.execute(sql, (self.tg_id,), fetchone=True)
        if data:
            print("Такой пользователь уже есть ) ")
        else:
            sql = """INSERT INTO sport(tg_id,name,datetime, status) VALUES (?,?,?,?)"""
            self.execute(sql, (self.tg_id, self.name, self.datetime, self.status), commit=True)