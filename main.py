print('привет!\nпогладь котю: он очень хочет этого')
print('серьёзно!\nгладь сейчас же!')
print('а кот-то ещё не поглажен...\nГЛАДЬ СЕЙЧАС ЖЕ!!!!')
from tkinter import *
import turtle as t
t.color('#714B23')
t.forward(29)
root = Tk()
root.title("METANIT.COM")
root.geometry("800x800")

canvas = Canvas(bg="white", width=10, height=10)
canvas.pack(anchor=CENTER, expand=1)

root.mainloop()