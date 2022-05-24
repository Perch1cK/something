from tkinter import *

window = Tk()
window.title('Опрос')
window.geometry('170x130')

a = {}


def clk():
    btn.configure(bg='#FFFFFF')
    btn2.configure(bg='#FFFFFF')
    btn3.configure(bg='#FFFFFF')
    btn4.configure(bg='#FFFFFF')
    btn.configure(bg='#00FF00')
def clk2():
    btn.configure(bg='#FFFFFF')
    btn2.configure(bg='#FFFFFF')
    btn3.configure(bg='#FFFFFF')
    btn4.configure(bg='#FFFFFF')
    btn2.configure(bg='#FF0000')
    btn.configure(bg='#00FF00')
def clk3():
    btn.configure(bg='#FFFFFF')
    btn2.configure(bg='#FFFFFF')
    btn3.configure(bg='#FFFFFF')
    btn4.configure(bg='#FFFFFF')
    btn3.configure(bg='#FF0000')
    btn.configure(bg='#00FF00')
def clk4():
    btn.configure(bg='#FFFFFF')
    btn2.configure(bg='#FFFFFF')
    btn3.configure(bg='#FFFFFF')
    btn4.configure(bg='#FFFFFF')
    btn4.configure(bg='#FF0000')
    btn.configure(bg='#00FF00')

lbl = Label(text='КТО ТАКОЙ ХАГИ ВАГИ?')
lbl.place(x=2, y=2)
btn = Button(text='СИНИЙ', command=clk)
btn.place(x=2, y=22)
btn2 = Button(text='ЧЕРНЫЙ', command=clk2)
btn2.place(x=2, y=42)
btn3 = Button(text='РОЗОВЫЙ', command=clk3)
btn3.place(x=2, y=62)
btn4 = Button(text='ЗЕЛЕНЫЙ',  command=clk4)
btn4.place(x=2, y=82)

window.mainloop()