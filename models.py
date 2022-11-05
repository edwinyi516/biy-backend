from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase("biy.sqlite")

class User(UserMixin, Model):
    email = CharField(unique = True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe = True)
    print("Connected to DB and created tables if they don't already exist")
    DATABASE.close()