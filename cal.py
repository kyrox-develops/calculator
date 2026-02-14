from _tkinter import *
expr=""
def press(key):
    global expr
    expr+=str(key)
    display.set(expr)
