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
    Entry
