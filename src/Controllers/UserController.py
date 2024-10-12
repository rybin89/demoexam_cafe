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
    def upadate_status_true(self):
        Users.update({Users.status: True}).execute()

    @classmethod
    def show(cls,login):
        return Users.get(Users.login==login)
#     Вывод списка в зависимости от роли
    @classmethod
    def show_user(cls,role_id):
        return Users.select().where(Users.role_id == role_id)
    @classmethod
    def list_user(cls, role_id):
        list = []
        for user in UserController.show_user(role_id):
            list.append(user.login)
        return list

if __name__ == "__main__":
    for row in UserController.show_user(3):
        print(row.login)
    print(UserController.list_user(3))