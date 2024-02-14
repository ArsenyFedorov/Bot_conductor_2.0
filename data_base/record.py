import sqlite3
from data_base.data_base import DataBase
from aiogram.types import Message
import datetime


class Record(DataBase):

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS record_history
                                 (tg_id INTEGER, name TEXT,
                                 id_work INTEGER PRIMARY KEY AUTOINCREMENT,
                                 datetime DATETIME, status TEXT)'''
        Record.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM record_history WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        records = self.execute(sql, parameters, fetchall=True)
        return records

    def save(self, date: datetime, status: str):
        sql = """UPDATE record_history SET status=? WHERE datetime=?"""
        self.execute(sql, (status, date), commit=True)

    def create(self, tg_id: int, name: str, date, status: str):
        sql = """SELECT * FROM record_history WHERE datetime=? AND tg_id=?"""
        data = self.execute(sql, (date, tg_id), fetchone=True)
        if data:
            print("Пользователь с таким занятием уже есть )")
        else:
            sql = """INSERT INTO record_history(tg_id,name,datetime, status) VALUES (?,?,?,?)"""
            self.execute(sql, (tg_id, name, date, status), commit=True)
