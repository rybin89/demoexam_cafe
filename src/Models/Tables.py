# Модель описывающая сущность из таблицы столы
from src.Models.Base import *

class Tables(Base):
    id = PrimaryKeyField()
    number = IntegerField()