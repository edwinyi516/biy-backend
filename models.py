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

class Module(Model):
    user = ForeignKeyField(User, backref = 'modules')
    i_value = CharField()
    category = CharField()
    transactiontype = CharField()
    interval = CharField()
    frequency = CharField()

    class Meta:
        database = DATABASE

class Expense(Model):
    user = ForeignKeyField(User, backref = 'expenses')
    recurring = BooleanField()
    frequency = CharField()
    date = DateField()
    amount = IntegerField()

    class Meta:
        database = DATABASE

class Income(Model):
    user = ForeignKeyField(User, backref = 'incomes')
    recurring = BooleanField()
    frequency = CharField()
    date = DateField()
    amount = IntegerField()

    class Meta:
        database = DATABASE

class Bill(Model):
    user = ForeignKeyField(User, backref = 'bills')
    paid = BooleanField()
    recurring = BooleanField()
    frequency = CharField()
    due_date = DateField()

    class Meta:
        database = DATABASE

class Goal(Model):
    user = ForeignKeyField(User, backref = 'goals')
    name = CharField()
    amount = IntegerField()
    percentage_completed = IntegerField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Layout, Module, Expense, Income, Bill, Goal], safe = True)
    print("Connected to DB and created tables if they don't already exist")
    DATABASE.close()