#!/usr/bin/env python3.4
from tkinter import *
import parser
import stack


root = Tk()
root.title('Calculator')

i = 0

def factorial():
    """Calculates the factorial of the number entered."""
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number 
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, END)

def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)
root.columnconfigure(2,pad=3)
root.columnconfigure(3,pad=3)
root.columnconfigure(4,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)
root.rowconfigure(2,pad=3)
root.rowconfigure(3,pad=3)

display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 6    , sticky = W+E)

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

cls = Button(root, text = "AC", command = clear_all, font=("Calibri", 12), foreground = "red")
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

# adding new operations
pi = Button(root, text = "pi", command = lambda: get_operation("*3.14"), font =("Calibri", 12))
pi.grid(row = 2, column = 4)
modulo = Button(root, text = "%", command = lambda :  get_operation("%"), font=("Calibri", 12))
modulo.grid(row = 3, column = 4)
left_bracket = Button(root, text = "(", command = lambda: get_operation("("), font =("Calibri", 12))
left_bracket.grid(row = 4, column = 4)
exp = Button(root, text = "exp", command = lambda: get_operation("**"), font = ("Calibri", 10))
exp.grid(row = 5, column = 4)

## To be added :
# sin, cos, log, ln
undo_button = Button(root, text = "<-", command = undo, font =("Calibri", 12), foreground = "red")
undo_button.grid(row = 2, column = 5)
fact = Button(root, text = "x!", command = factorial, font=("Calibri", 12))
fact.grid(row = 3, column = 5)
right_bracket = Button(root, text = ")", command = lambda: get_operation(")"), font =("Calibri", 12))
right_bracket.grid(row = 4, column = 5)
square = Button(root, text = "^2", command = lambda: get_operation("**2"), font = ("Calibri", 10))
square.grid(row = 5, column = 5)

root.mainloop()