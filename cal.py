from tkinter import *
from tkinter import Tk
expr=""
def press(key):
    global expr
    expr+=str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr=""
    except:
        display.set("error")
        expr=""

def clr():
    global expr
    expr=""
    display.set("")



if __name__=="__main__":
    tk=Tk()
    tk.configure(bg="red")
    tk.title("io calc")
    tk.geometry("270x150")

    display=StringVar()
    entry=Entry(tk,textvariable=display)
    entry.grid(columnspan=4,ipadx=70)


    btn1 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(1),hight=1,width=7)
    btn1.Grid(row=2,column=0)

    btn2 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(2),hight=1,width=7)
    btn2.Grid(row=2,column=1)

    btn3 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(3),hight=1,width=7)
    btn3.Grid(row=2,column=2)

    btn4 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(4),hight=1,width=7)
    btn4.Grid(row=2,column=0)

    btn5 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(5),hight=1,width=7)
    btn5.Grid(row=2,column=0)

    btn6 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(6),hight=1,width=7)
    btn6.Grid(row=2,column=1)

    btn7 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(7),hight=1,width=7)
    btn7.Grid(row=2,column=2)

    btn8 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(8),hight=1,width=7)
    btn8.Grid(row=2,column=3)

    btn9 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(9),hight=1,width=7)
    btn9.Grid(row=2,column=0)

    btn0 =Button(tk,text='1',fg='blue',bg='black',COMMAND=lambda: press(0),hight=1,width=7)
    btn0.Grid(row=2,column=1)
