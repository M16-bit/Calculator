import sys
from tkinter import *
#from PIL import ImageTk, Image

root = Tk()
#root.geometry("300x100")
root.title("Simple Calculator")
root.iconbitmap('Sigma.ico')
#print(sys.version)
flag = True
e = Entry(root, text="0")
e.grid(row=0, column=0, columnspan=3)


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
    elif op == "X":
        e.insert(0, int(x) * fnum)
    else:
        e.delete(0, END)
    global flag
    flag = False


button_1 = Button(root, text="1", command=lambda: clicknum(1), width=11, height=3)
button_2 = Button(root, text="2", command=lambda: clicknum(2), width=11, height=3)
button_3 = Button(root, text="3", command=lambda: clicknum(3), width=11, height=3)
button_4 = Button(root, text="4", command=lambda: clicknum(4), width=11, height=3)
button_5 = Button(root, text="5", command=lambda: clicknum(5), width=11, height=3)
button_6 = Button(root, text="6", command=lambda: clicknum(6), width=11, height=3)
button_7 = Button(root, text="7", command=lambda: clicknum(7), width=11, height=3)
button_8 = Button(root, text="8", command=lambda: clicknum(8), width=11, height=3)
button_9 = Button(root, text="9", command=lambda: clicknum(9), width=11, height=3)
button_0 = Button(root, text="0", command=lambda: clicknum(0), width=11, height=4)

button_clear = Button(root, text="Clear", command=clear, width=11, height=4).grid(row=4, column=0)
button_plus = Button(root, text="+", command=lambda: clickop("+"), width=11, height=4).grid(row=5, column=0)
button_equal = Button(root, text="=", command=comp, width=11, height=4).grid(row=4, column=2)
button_minus = Button(root, text="-", command=lambda: clickop("-"), width=11, height=4).grid(row=5, column=1)
button_prod = Button(root, text="X", command=lambda: clickop("X"), width=11, height=4).grid(row=5, column=2)

button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

Msg = Label(root, text="Made by Harshit Joshi", font=("Times", 20, "italic"))

root.mainloop()
