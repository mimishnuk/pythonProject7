import sqlite3
from sqlite3 import Connection

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("connect")

    db.execute("CREATE TABLE IF NOT EXISTS  mentors"
               "(id INTEGER PRIMARY KEY,"
               "username TEXT, "
               "fullname TEXT,"
               "direction TEXT,"
               "age INTEGER,"
               "grouppa INTEGER)")
    db.commit()

async def sqlite_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()












