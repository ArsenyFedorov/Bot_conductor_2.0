import sqlite3


class DataBase:
    db_path = "data_base\sport.db"

    @staticmethod
    def execute(sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = sqlite3.connect(DataBase.db_path)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        if commit:
            connection.commit()
        connection.close()
        return data

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict, _and: bool = True) -> tuple:
        sql += ('AND' if _and else ', ').join([f"{key}= ?" for key in parameters])
        return sql, tuple(parameters.values())

# СОЗДАНИЕ ТАБЦИЦЫ
# def database_connect():
#     connection = sqlite3.Connection(PATH)
#     cursor = connection.cursor()
#
#     cursor.execute('''CREATE TABLE IF NOT EXISTS sport
#                     (tg_id INTEGER, name TEXT,
#                     id_work INTEGER PRIMARY KEY AUTOINCREMENT,
#                     datetime ,direction TEXT,status TEXT)''')
#     connection.commit()
#
# ДОБАВЛЕНИЕ ЗНАЧЕНИЯ В ТАБЛИЦУ
# def add_user(id_user: int, name: str):
#     connection = sqlite3.Connection(PATH)
#     cursor = connection.cursor()
#     sql = """INSERT INTO sport(tg_id,name) VALUES(?,?)"""
#     cursor.execute(sql, (id_user, name))
#     connection.commit()
#
# ПОЛУЧЕНИЕ ЗНАЧЕНИЯ ИЗ ТАБЛИЦЫ
# def select_users(tg_id: int):
#     connection = sqlite3.Connection(PATH)
#     cursor = connection.cursor()
#     sql = """SELECT * FROM sport WHERE tg_id=?"""
#     id_user = cursor.execute(sql, (tg_id,)).fetchone()
#     return id_user