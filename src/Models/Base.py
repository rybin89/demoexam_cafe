#Базовая модель peewee
from peewee import *
from src.Connection.connect import *


class Base(Model):
    class Meta:
        database = database()




