from peewee import Model
from peewee import SqliteDatabase
from peewee import CharField

db = SqliteDatabase('database.sqlite3')


class Users(Model):
    vk_id = CharField()
    telegram_id = CharField()

    class Meta:
        database = db


Users.create_table()
