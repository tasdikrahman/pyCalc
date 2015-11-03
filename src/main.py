#!/usr/bin/env python3.4

from tkinter import *

root = Tk()
root.title('Calculator')

i = 0

def clear_all():
    display.delete(0, END)

def get_variables(num):
    """
        note to self:
        I have to declare i as global here as the value of i would be copied to a local variable
        for the function get_variables() and not updated from 0.

        so we tell python to lookup for i in scopes other than that of this function
        ref : http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
    """    
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i
    display.insert(i, operator)
    i += 1

def calculate():
    whole_string = display.get()
    if "+" in whole_string:
        var1, var2 = whole_string.split("+")
        clear_all()
        result = int(var1) + int(var2)
        display.insert(0,result)
    elif "-" in whole_string:
        var1, var2 = whole_string.split("-")
        clear_all()
        result = int(var1) - int(var2)
        display.insert(0, result)
    elif "*" in whole_string:
        var1, var2 = whole_string.split("*")
        clear_all()
        result = int(var1) * int(var2)
        display.insert(0, result)
    elif "/" in whole_string:
        var1, var2 = whole_string.split("/")
        clear_all()

        try:
            result = int(var1) / int(var2)
            display.insert(0, result)

        except Exception:
            display.insert(0, "Zero division error!")


root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)
root.columnconfigure(2,pad=3)
root.columnconfigure(3,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)
root.rowconfigure(2,pad=3)
root.rowconfigure(3,pad=3)

display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 4, sticky = W+E)

one = Button(root, text = "1", command = lambda : get_variables(1), font=("Calibri", 12))
one.grid(row = 2, column = 0)
two = Button(root, text = "2", command = lambda : get_variables(2), font=("Calibri", 12))
two.grid(row = 2, column = 1)
three = Button(root, text = "3", command = lambda : get_variables(3), font=("Calibri", 12))
three.grid(row = 2, column = 2)

four = Button(root, text = "4", command = lambda : get_variables(4), font=("Calibri", 12))
four.grid(row = 3 , column = 0)
five = Button(root, text = "5", command = lambda : get_variables(5), font=("Calibri", 12))
five.grid(row = 3, column = 1)
six = Button(root, text = "6", command = lambda : get_variables(6), font=("Calibri", 12))
six.grid(row = 3, column = 2)

seven = Button(root, text = "7", command = lambda : get_variables(7), font=("Calibri", 12))
seven.grid(row = 4, column = 0)
eight = Button(root, text = "8", command = lambda : get_variables(8), font=("Calibri", 12))
eight.grid(row = 4, column = 1)
nine = Button(root , text = "9", command = lambda : get_variables(9), font=("Calibri", 12))
nine.grid(row = 4, column = 2)

cls = Button(root, text = "cls", command = clear_all, font=("Calibri", 12))
cls.grid(row = 5, column = 0)
zero = Button(root, text = "0", command = lambda : get_variables(0), font=("Calibri", 12))
zero.grid(row = 5, column = 1)
result = Button(root, text = "=", command = calculate, font=("Calibri", 12), foreground = "red")
result.grid(row = 5, column = 2)

plus = Button(root, text = "+", command =  lambda : get_operation("+"), font=("Calibri", 12))
plus.grid(row = 2, column = 3)
minus = Button(root, text = "-", command =  lambda : get_operation("-"), font=("Calibri", 12))
minus.grid(row = 3, column = 3)
multiply = Button(root,text = "*", command =  lambda : get_operation("*"), font=("Calibri", 12))
multiply.grid(row = 4, column = 3)
divide = Button(root, text = "/", command = lambda :  get_operation("/"), font=("Calibri", 12))
divide.grid(row = 5, column = 3)

root.mainloop()