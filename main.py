from PIL import ImageTk
import tkinter as tk
from tkinter import *
import sys
import os

# Функция для получения пути к файлам в собранном приложении
def resource_path(relative_path):
    """Возвращает абсолютный путь к ресурсу, работает для разработки и в собранном .exe"""
    try:
        # PyInstaller создаёт временную папку, и путь доступен через sys._MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Если запускается не из .exe, используем текущую директорию
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Глобальная переменная для определения типа фигуры
count = 0
a = ''

# Внутренности интерфейса
def white():
    global a
    a = 'white'
def yellow():
    global a
    a = 'yellow'
def blue():
    global a
    a = 'blue'
def red():
    global a
    a = 'red'
def black():
    global a
    a = 'black'
def green():
    global a
    a = 'green'
def delete():
    canvas.delete(ALL)
    entry_x1.configure(state='disabled')
    entry_y1.configure(state='disabled')
    entry_x2.configure(state='disabled')
    entry_y2.configure(state='disabled')
    entry_x3.configure(state='disabled')
    entry_y3.configure(state='disabled')
    entry_x4.configure(state='disabled')
    entry_y4.configure(state='disabled')
def unlock2():
    entry_x1.configure(state='normal')
    entry_y1.configure(state='normal')
    entry_x2.configure(state='normal')
    entry_y2.configure(state='normal')
def line():
    unlock2()
    global count
    count += 2
def tri():
    entry_x1.configure(state='normal')
    entry_y1.configure(state='normal')
    entry_x2.configure(state='normal')
    entry_y2.configure(state='normal')
    entry_x3.configure(state='normal')
    entry_y3.configure(state='normal')
    global count
    count += 3
def square_empty():
    unlock2()
    global count
    count += 4
def square_hard():
    entry_x1.configure(state='normal')
    entry_y1.configure(state='normal')
    entry_x2.configure(state='normal')
    entry_y2.configure(state='normal')
    entry_x3.configure(state='normal')
    entry_y3.configure(state='normal')
    entry_x4.configure(state='normal')
    entry_y4.configure(state='normal')
    global count
    count += 5
def oval():
    unlock2()
    global count
    count += 6
def cat_face():
    global a
    canvas.create_polygon(170,200, 170,50, 220,130, 270,130, 320,50, 320, 200, 245, 230, outline=a, fill=a)
def create():
    valx1 = entry_x1.get()
    valy1 = entry_y1.get()
    valx2 = entry_x2.get()
    valy2 = entry_y2.get()
    valx3 = entry_x3.get()
    valy3 = entry_y3.get()
    valx4 = entry_x4.get()
    valy4 = entry_y4.get()
    global count
    global a
    if count == 2:
        canvas.create_line(valx1, valy1, valx2, valy2, outline=a)
    if count == 3:
        canvas.create_polygon(valx1, valy1, valx2, valy2, valx3, valy3, outline=a)
    if count == 4:
        canvas.create_rectangle(valx1, valy1, valx2, valy2, outline=a)
    if count == 5:
        canvas.create_polygon(valx1, valy1, valx2, valy2, valx3, valy3, valx4, valy4, outline=a)
    if count == 6:
        canvas.create_oval(valx1, valy1, valx2, valy2, outline=a)
    count = 0
    entry_x1.configure(state='disabled')
    entry_y1.configure(state='disabled')
    entry_x2.configure(state='disabled')
    entry_y2.configure(state='disabled')
    entry_x3.configure(state='disabled')
    entry_y3.configure(state='disabled')
    entry_x4.configure(state='disabled')
    entry_y4.configure(state='disabled')

# Свойства окна
win = tk.Tk()
icon = tk.PhotoImage(file=resource_path("compass icon.png"))  # Используем resource_path
win.iconphoto(False, icon)
win.title('PHE(Paint Height Edition)')
win.geometry('500x600+100+30')
win.resizable(False, False)

# Холст для рисования
canvas = Canvas(win, height=370, width=500, bg="white")
canvas.pack()

# Кнопки
x_dir = tk.Label(text='Points 1')
x_dir.place(x=58, y=375 + 115)
x_dir = tk.Label(text=' ⯆')
x_dir.place(x=73, y=390 + 115)
x_dir = tk.Label(text='P 2')
x_dir.place(x=62 + 58, y=375 + 115)
x_dir = tk.Label(text=' ⯆')
x_dir.place(x=120, y=390 + 115)
x_dir = tk.Label(text='P 3')
x_dir.place(x=62 + 58 + 49, y=375 + 115)
x_dir = tk.Label(text=' ⯆')
x_dir.place(x=168, y=390 + 115)
x_dir = tk.Label(text='P 4')
x_dir.place(x=62 + 58 + 49 + 49, y=375 + 115)
x_dir = tk.Label(text=' ⯆')
x_dir.place(x=218, y=390 + 115)
x_dir = tk.Label(text=' ⯈')
x_dir.place(x=40, y=412 + 115)
x_dir = tk.Label(text=' ⯈')
x_dir.place(x=40, y=437 + 115)
x_dir = tk.Label(text='X')
x_dir.place(x=32, y=412 + 115)
x_dir = tk.Label(text='y')
x_dir.place(x=32, y=437 + 115)

# Поля ввода
entry_x1 = tk.Entry(win, state='disabled')
entry_x1.place(x=60, y=415 + 115, width=40)
entry_y1 = tk.Entry(win, state='disabled')
entry_y1.place(x=60, y=440 + 115, width=40)
entry_x2 = tk.Entry(win, state='disabled')
entry_x2.place(x=110, y=415 + 115, width=40)
entry_y2 = tk.Entry(win, state='disabled')
entry_y2.place(x=110, y=440 + 115, width=40)
entry_x3 = tk.Entry(win, state='disabled')
entry_x3.place(x=160, y=415 + 115, width=40)
entry_y3 = tk.Entry(win, state='disabled')
entry_y3.place(x=160, y=440 + 115, width=40)
entry_x4 = tk.Entry(win, state='disabled')
entry_x4.place(x=210, y=415 + 115, width=40)
entry_y4 = tk.Entry(win, state='disabled')
entry_y4.place(x=210, y=440 + 115, width=40)

# Основной интерфейс
# Цвета
img_white = ImageTk.PhotoImage(file=resource_path('WHITE.png'))
btn_white = Button(win, image=img_white, command=white, bg='white')
img_blue = ImageTk.PhotoImage(file=resource_path('BLUE.png'))
btn_blue = Button(win, image=img_blue, command=blue, bg='white')
img_yellow = ImageTk.PhotoImage(file=resource_path('YELLOW.png'))
btn_yellow = Button(win, image=img_yellow, command=yellow, bg='white')
img_red = ImageTk.PhotoImage(file=resource_path('RED.png'))
btn_red = Button(win, image=img_red, command=red, bg='white')
img_black = ImageTk.PhotoImage(file=resource_path('BLACK.png'))
btn_black = Button(win, image=img_black, command=black, bg='white')
img_green = ImageTk.PhotoImage(file=resource_path('GREEN.png'))
btn_green = Button(win, image=img_green, command=green, bg='white')

# Фигуры и остальное
delete = tk.Button(win, text='Delete all', command=delete, bg='red', fg='#FFFAFA', font=("Verdana", 13, "bold"))
go = tk.Button(win, text='Create', command=create, bg='#00BFFF', fg='#FFFAFA', font=("Verdana", 13, "bold"))
img2 = ImageTk.PhotoImage(file=resource_path('Линия.png'))
btn2 = Button(win, image=img2, command=line, bg='white')
img3 = ImageTk.PhotoImage(file=resource_path('Треугольник.png'))
btn3 = Button(win, image=img3, command=tri, bg='white')
img4 = ImageTk.PhotoImage(file=resource_path('Квадрат.png'))
btn4 = Button(win, image=img4, command=square_empty, bg='white')
img5 = ImageTk.PhotoImage(file=resource_path('Параллелепипед.png'))
btn5 = Button(win, image=img5, command=square_hard, bg='white')
img6 = ImageTk.PhotoImage(file=resource_path('Овал.png'))
btn6 = Button(win, image=img6, command=oval, bg='white')
img_cat = ImageTk.PhotoImage(file=resource_path('cat face.png'))
btn_cat = Button(win, image=img_cat, command=cat_face, bg='white')

btn2.place(x=330, y=520, width=60, height=60)
btn3.place(x=330, y=450, width=60, height=60)
btn4.place(x=400, y=450, width=60, height=60)
btn5.place(x=400, y=520, width=60, height=60)
btn6.place(x=260, y=520, width=60, height=60)
btn_blue.place(x=270 - 9, y=425)
btn_yellow.place(x=245 - 9, y=425)
btn_white.place(x=220 - 9, y=425)
btn_red.place(x=270 - 9, y=450)
btn_green.place(x=245 - 9, y=450)
btn_black.place(x=220 - 9, y=450)
btn_cat.place(x=60, y=375)
go.pack()
delete.place(x=380, y=375)

win.mainloop()
