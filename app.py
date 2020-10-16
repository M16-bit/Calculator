import sys
from tkinter import *
#from PIL import ImageTk, Image

BN_WIDTH = 8
BN_HEIGHT = 3

root = Tk()
#root.geometry("300x100")
root.title("Simple Calculator")
root.iconbitmap('Sigma.ico')
#print(sys.version)
flag = True
e = Entry(root, text="0", width=BN_WIDTH*3)
e.grid(row=0, column=0, columnspan=4)


def clicknum(number):
    global flag
    if not flag:
        e.delete(0, END)
    x = e.get()
    e.delete(0, END)
    e.insert(0, str(x)+str(number))
    flag = True


def clear():
    e.delete(0, END)


def clickop(sign):
    x = e.get()
    e.delete(0, END)
    global op
    op = sign
    global fnum
    fnum = int(x)


def comp():
    x = e.get()
    e.delete(0, END)
    if op == "+":
        e.insert(0, int(x) + fnum)
    elif op == "-":
        e.insert(0, fnum - int(x))
    elif op == "x":
        e.insert(0, int(x) * fnum)
    elif op == "÷":
        e.insert(0, fnum / int(x))
    else:
        e.delete(0, END)
    global flag
    flag = False


def create_button(text, command, row, column):
    button = Button(
        root, text=text, command=command, width=BN_WIDTH, height=BN_HEIGHT
    )
    button.grid(row=row, column=column)


def create_num_buttons():
    for num in range(10):
        rows = [4,3,3,3,2,2,2,1,1,1]
        cols = [0,0,1,2,0,1,2,0,1,2]
        command=lambda num=num: clicknum(num)
        create_button(str(num), command, rows[num], cols[num])  


def create_operator_buttons():
    operators = ['+', '-', 'x', '÷']
    rows = [4, 3, 2, 1]
    column = 3
    for operator, row in zip(operators, rows):
        command = lambda operator=operator: clickop(operator)
        create_button(operator, command, row, column)


create_num_buttons()
create_operator_buttons()
create_button(text="Clear", command=clear, row=4, column=1)
create_button(text="=", command=comp, row=4, column=2)


Msg = Label(root, text="Made by Harshit Joshi", font=("Times", 20, "italic"))

root.mainloop()
