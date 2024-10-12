# Окно авторизации с помощью библиотеки Tkinter
from pyexpat.errors import messages
from tkinter import *
from src.Controllers.UserController import *
from src.Tkinter.AdminPanel import *
# Функцианал
def click_test():
    button_login.configure(text="Нажал")
    message.configure(text=log_in.get(), font=(16),foreground='red')
    log_in.selection_clear()
# функция авторизации
def login():
    user = UserController()
    result = user.log_in(log_in.get(),passwd_in.get())
    if result:
        log = UserController.show(log_in.get()).role_id.id
        if log == 1:
            admin()
        elif log == 2:
            print("Cook")
        else:
            print("Oficiant")
    else:
        print("неверно введён Логин или пароль")
    print(result)

# Открыть новое окно из следующего файла tkinter
def open_window(window):
    pass
# Оформление окна
x_pixel = 800
y_pixel = 600

window = Tk() # вызываем класс tkinter
window.title("Информационная cиcтема КАФЕ") # создаём название окна
window.geometry(f'{x_pixel}x{y_pixel}')

title = Label(window, text="Привествуем в информационной \n системе КАФЕ", font=("Times New Roman",16))
title.update()
title.grid(columnspan = 12,column = 0, row = 0, padx = x_pixel/2 - 305/2) #координаты текста в окне

print(title.winfo_width())
# кнопки
button_login = Button(window,
                      text="Войти",
                      height = 2,
                      width = 8,
                      background = 'green',
                      foreground = 'white',
                      command=lambda: login)
button_login.grid(column = 0, row = 1)
message = Label(text = '')
message.grid(column = 0, row=4)
# окна ввода данных
log_title = Label(window,text="Введите логин")
log_title.grid(column = 0, row = 5)
log_in = Entry(window, width = 20)
log_in.grid(column = 1, row = 5)
passwd_title = Label(window,text="Введите пароль")
passwd_title.grid(column = 0, row = 6)
passwd_in = Entry(window,width = 20)
passwd_in.grid(column = 1, row = 6)


window.mainloop()# запускаем окно
