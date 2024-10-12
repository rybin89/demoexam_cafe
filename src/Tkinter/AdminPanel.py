# Окно - Панель Администратора
import os
from tkinter import *
from tkinter import ttk
from src.Controllers.ShiftController import ShiftController
from src.Controllers.UserController import UserController



def admin():
    # функционал
    # создание диалогового окна
    def status_false(id):
        button_login.configure(text="Уволен", background='grey')
        user.upadate_status(id)
        update()
    def add_user(login,name,passwd,role):
        user.add(login,passwd,name,role)
        panel_admin.after(1000,update)

    # обновление окна
    def update():
        panel_admin.destroy()
        admin()
    # функция создания смен
    def add_shift(date, cook, oficiant1, oficiant2):
        print(date, cook, oficiant1, oficiant2)

    #     объект смены
    shift = ShiftController()
    # отрисовка
    panel_admin = Tk()
    panel_admin.geometry("2000x800")
    panel_admin.title("Панель администора")
    # Заголовок
    title_window = Label(panel_admin, text='Панель администора',font=("Times New Roman",24))
    title_window.grid(column = 0, row = 0, columnspan = 12,padx = 400, pady = 10)
    # title_window.pack(expand = True, anchor = N,side = TOP)
    # Сотрудники
    title_employee = Label(panel_admin, text= "Сотрудники", font= (20))
    # title_employee.pack(expand = True, side = TOP)
    title_employee.grid(column = 1, row = 1, padx = 10, pady = 10)
    # логин должность и кнопка
    user = UserController()
    list_user = user.get()
    count_row = 2
    for row in list_user:
        if row.status:
            login_title = Label(panel_admin, text= row.login)
            login_title.grid(column = 0, row = count_row, padx = 1, pady = 1)
            login_role = Label(panel_admin, text=row.role_id.role)
            login_role.grid(column=2, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                                  text="Уволить",
                                  height=2,
                                  width=8,
                                  background='red',
                                  foreground='white',
                                  # command = lambda id = row.id: user.upadate_status(id))
                                  command = lambda id = row.id: status_false(id))

            status_title = Label(panel_admin, text=row.id)
            status_title.grid(column=4, row=count_row, padx=0, pady=1)
            button_login.grid(column=3, row=count_row, padx=0, pady=1)

        else:
            login_title = Label(panel_admin, text=row.login)
            login_title.grid(column=0, row=count_row, padx=1, pady=1)
            login_role = Label(panel_admin, text=row.role_id.role)
            login_role.grid(column=2, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                                  text="Уволен",
                                  height=2,
                                  width=8,
                                  background='grey',
                                  foreground='white',
                                  # command = lambda id = row.id: user.upadate_status(id))
                                  command=lambda id=row.id: status_false(id))

            status_title = Label(panel_admin, text=row.id)
            status_title.grid(column=4, row=count_row, padx=0, pady=1)
            button_login.grid(column=3, row=count_row, padx=0, pady=1)
        count_row +=1
    # Добавить пользователя

    input_login = Entry(panel_admin,width=20)
    name_input_login = Label(panel_admin,text="Введите логин")
    name_input_login.grid(column=5,row=2)
    input_login.grid(column=5,row=3)

    input_name = Entry(panel_admin, width=20)
    name_input_name  = Label(panel_admin, text="Введите имя")
    name_input_name .grid(column=5, row=4)
    input_name .grid(column=5, row=5)

    input_password = Entry(panel_admin, width=20)
    name_input_password= Label(panel_admin, text="Введите пароль")
    name_input_password.grid(column=5, row=6)
    input_password.grid(column=5, row=7)

    input_role = Entry(panel_admin, width=20)
    name_input_role = Label(panel_admin, text="Введите должность")
    name_input_role.grid(column=5, row=8)
    input_role.grid(column=5, row=9)

    button_add_user = Button(panel_admin, text="Добавить пользователя",height=2,width=20,
                             background='green',foreground='white',
                             command = lambda: add_user(input_login.get(),input_name.get(),
                                                        input_password.get(),input_role.get()))
    button_add_user.grid(column = 5, row = 10)

    # вывод смен
    title_shifts = Label(panel_admin,text="Смены")
    title_shifts.grid(column = 6, row= 1, columnspan = 4)
    dount_shift = 2
    for shift in shift.get():
        date = Label(panel_admin, text = shift.date)
        cook_id = Label(panel_admin, text = shift.cook_id.name)
        oficiant_1_id = Label(panel_admin, text = shift.oficiant_1_id.name)
        oficiant_2_id = Label(panel_admin, text = shift.oficiant_2_id.name)

        date.grid(column = 6, row = dount_shift)
        cook_id.grid(column = 7, row = dount_shift)
        oficiant_1_id.grid(column = 8, row = dount_shift)
        oficiant_2_id.grid(column = 9, row = dount_shift)
        dount_shift+=1

    #     Добавить смену
    title_cook = Label(panel_admin, text="Выберите повара")
    title_cook.grid(column = 10, row = 2)
    # вывод поваров в виде списка

    def selected(event):
        # получаем выделенный элемент
        selection = combobox_cook.get()
        print(selection)

        label["text"] = f"вы выбрали: {selection}"
        return selection

    list_cook = UserController.list_user(2)
    one_element = StringVar(value=list_cook[0])
    label = Label(textvariable=one_element)
    label.grid(column = 11, row = 2)
    combobox_cook = ttk.Combobox(values=list_cook, textvariable=one_element)
    combobox_cook.grid(column = 10, row = 3)
    date_input = combobox_cook.bind("<<ComboboxSelected>>", selected)
    cook_input = combobox_cook.get()
    oficiant1_input = combobox_cook.get()
    oficiant2_input = combobox_cook.get()
    # combobox_cook.bind("<<ComboboxSelected>>", selected)
    add_shift_button = Button(panel_admin, text="Добавить смену", height=2,width=20,
                             background='blue',foreground='white',
                             command= lambda date = date_input , cook=cook_input , oficiant1 = oficiant1_input , oficiant2 = oficiant2_input: add_shift(date, cook, oficiant1, oficiant2))
    add_shift_button.grid(column = 10, row = 10)

    panel_admin.mainloop()
if __name__ == "__main__":
    admin()