from src.Models.Orders import *
from src.Models.Users import Users


class OrderController:

    #  изменить стастус на готов
    @classmethod
    def update_order_ready(cls, order_id):
        Orders.update({Orders.status_id : 4}).where(Orders.id == order_id).execute()
#   изменить статус на оплачен
    @classmethod
    def update_order_pay(cls,order_id):
        Orders.update({Orders.status_id : 2}).where(Orders.id == order_id).execute()
    # метод вывода заказов ЗАДАННОЙ смены
    @classmethod
    def show(cls,shift_id):
        return Orders.select().where(Orders.shift_id == shift_id)
    #  изменить стастус на готовИтся
    @classmethod
    def update_order_cooking(cls,order_id):
        Orders.update({Orders.status_id : 3}).where(Orders.id == order_id).execute()

     # вывести спиок заказов
    @classmethod
    def get(cls):
        return Orders.select()
#     создать заказ
    @classmethod
    def add_order(cls,count_clients,table_id,drink_id,food_id,shift_id):
        Orders.create(count_clients = count_clients,
                      table_id =table_id,
                      drink_id = drink_id,
                      food_id = food_id,
                      shift_id = shift_id,
                      status_id = 1)
if __name__ == "__main__":
    # OrderController.update_order_ready(2)
    # OrderController.update_order_pay(2)
    # for order in OrderController.show(2):
    #     print(order.id, order.count_cliens,order.table_id,order.drink_id.name, order.status_id.name)
    # OrderController.update_order_cooking(2)
    # for order in OrderController.show(2):
    #     print(order.id, order.count_cliens,order.table_id,order.drink_id.name, order.status_id.name)
    for order in OrderController.get():
        print(order.id, order.count_cliens, order.table_id, order.drink_id.name, 'Статус заказа:',order.status_id.name, 'Еда', order.food_id.name)

    OrderController.add_order(3,3,5,1,2)
    for order in OrderController.get():
        print(order.id, order.count_cliens, order.table_id, order.drink_id.name, 'Статус заказа:',order.status_id.name, 'Еда', order.food_id.name)