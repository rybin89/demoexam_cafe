from peewee import *
from pymysql import *

def database():
    mysql_db = MySQLDatabase('rybin_de_ex_c',
                         user='rybin_adcafe',
                         password='111111',
                         host='10.11.13.118',
                         port=3306)
    return mysql_db


if __name__ == "__main__":
    database().connect()

