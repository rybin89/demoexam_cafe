from src.Models.Shifts import *
from src.Controllers.UserController import UserController

class ShiftController():

    # Создание СМЕНЫ
    def add(self, datetime, cook, oficiant_1, oficiant_2):
        cook_id = UserController.show(cook)
        oficiant_1_id = UserController.show(oficiant_1)
        oficiant_2_id = UserController.show(oficiant_2)
        print(type(cook_id))
        print(cook_id.id)
        Shifts.create(datetime = datetime, cook_id = cook_id.id, oficiant_1_id = oficiant_1_id.id, oficiant_2_id = oficiant_2_id.id)

    #вывод смены
    def get(self):
        return Shifts.select()


if __name__ == "__main__":
    sh = ShiftController()
    for row in sh.get():
        print(row.id, row.cook_id.login, row.oficiant_1_id.login, row.oficiant_2_id.login)
    print("-------------------------------")
    sh.add('2024-10-04 10:00:00', 'cook_Alexandr', 'waiter_Sergey', 'waiter_Ilya')
    for row in sh.get():
        print(row.id, row.cook_id.login, row.oficiant_1_id.login, row.oficiant_2_id.login, row.date)