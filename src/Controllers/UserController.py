#Управление пользователями

from src.Models.Users import *

class UserController():
    # метод авторизации
    def log_in(self,input_login,input_password):

        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False
    # Вывоз пользователей
    def get(self):
        return Users.select().execute()
    # Добавить пользователя
    def add(self,input_login, input_password,input_name, input_role_id):
        Users.create(login = input_login, password = input_password, name = input_name, role_id = input_role_id)
    # Уволить - изменить статус на False
    def upadate_status(self, id_user):
        Users.update({Users.status : False}).where(Users.id == id_user).execute()
    # метод который выводит id по имени
    # метод КЛАССА
    @classmethod
    def show(cls,login):
        return Users.get(Users.login==login)
if __name__ == "__main__":
    users = UserController()
    print(users.log_in('admin_Ekaterina','111111'))
    for row in users.get():
        print(row.login)
    # users.add('IVAN', '123456', "Ivanow IVAN", 1)
    for row in users.get():
        print(row.id, row.login, row.status)
    users.upadate_status(9)
    for row in users.get():
        print(row.id, row.login, row.status)
    print(users.show('IVAN'))