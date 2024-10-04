from peewee import *

connect = MySQLDatabase(
    'rybin_de_ex_c',
    user = 'rybin_adcafe',
    password = '111111',
    host = '10.11.13.118',
    port = 3306

)

if __name__ == "__main__":
    connect.connect()