import os
from peewee import *
from flask_login import UserMixin
from playhouse.db_url import connect

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///biy.sqlite')

class User(UserMixin, Model):
    email = CharField(unique = True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()

    class Meta:
        database = DATABASE

class Layout(Model):
    user = ForeignKeyField(User, backref = 'layouts')
    layout_data = CharField()

    class Meta:
        database = DATABASE

class Category(Model):
    user = ForeignKeyField(User, backref = 'category')
    name = CharField()

    class Meta:
        database = DATABASE

class Expense(Model):
    user = ForeignKeyField(User, backref = 'expense')
    category = ForeignKeyField(Category, backref = 'expense')
    recurring = BooleanField()
    fixed = BooleanField()
    frequency = CharField()
    amount = IntegerField()

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Layout, Category, Expense], safe = True)
    print("Connected to DB and created tables if they don't already exist")
    DATABASE.close()