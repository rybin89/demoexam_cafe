from src.Models.Orders import *
from src.Models.Users import Users


class OrderController:

    #  изменить стастус на готов
    @classmethod
    def update_order_ready(cls, order_id):
        Orders.update({Orders.status_id : 4}).where(Orders.id == order_id).execute()

if __name__ == "__main__":
    OrderController.update_order_ready(2)