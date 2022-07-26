###########################################################
#   Application: Calculator Application                   #
#   Author: Kevin Nguyen                                  #

# import libraries
from tkinter import *
# import message boxes
import tkinter.messagebox as messagebox
# import Treeview
import tkinter.ttk as ttk
# import database from python file CRUDdatabase
# from CRUDdatabase import Database

# create a window
root = Tk()
# add title to application
root.title("Calculator")
# size application window
root.geometry("400x530")

# define variable for text display
textDisplay = StringVar()
textDisplay.set("0")

# define current_input variable
current_input = ""

# define first number to be operated on
number_to_operate = ""

# define selected operator
operator = ""

# define if equals was pressed
equalCheck = ""

# define results of calculation
result = ""

# define functions for button commands
# clear the display and reset the current input
def clearDisplay():
    textDisplay.set("0")
    global current_input
    current_input = ""

# assign value to current input
def number(string_number):
    global equalCheck
    global current_input
    # check if need to clear label box if previous arithmetic operations was performed
    if equalCheck == True:
        clearDisplay()
        equalCheck = False
    textDisplay.set(current_input + string_number)
    current_input += string_number

# assign negative to current input
def negative():
    global current_input
    textDisplay.set("-" + current_input)
    current_input = "-" + current_input

# addition
def addition():
    global current_input
    global number_to_operate
    global operator
    number_to_operate = float(current_input)
    operator = "+"
    #clear the current input so that another input can be assigned
    clearDisplay()

def subtraction():
    global current_input
    global number_to_operate
    global operator
    number_to_operate = float(current_input)
    operator = "-"
    #clear the current input so that another input can be assigned
    clearDisplay()

def multiply():
    global current_input
    global number_to_operate
    global operator
    number_to_operate = float(current_input)
    operator = "*"
    #clear the current input so that another input can be assigned
    clearDisplay()

def divide():
    global current_input
    global number_to_operate
    global operator
    number_to_operate = float(current_input)
    operator = "/"
    #clear the current input so that another input can be assigned
    clearDisplay()

def equal():
    global current_input
    global number_to_operate
    global operator
    global equalCheck
    global result
    if current_input == "":
        current_input = 0
    else:
        current_input = float(current_input)
    # check which type of operator and perform that operation on two numbers
    if operator == "+":
        result = number_to_operate + current_input
    if operator == "-":
        result = number_to_operate - current_input
    if operator == "*":
        result = number_to_operate * current_input
    if operator == "/":
        # check if divison by zero
        if current_input == 0:
            textDisplay.set("Cannot divide by zero.")
            return
    # limit decimal places in result to 10 digits
    result = round(result,10)
    textDisplay.set(result)
    # set equalCheck to True. This will be used to clear the calculator later.
    equalCheck = True

def percentage():
    global result
    percent = result*100
    textDisplay.set(str(percent)+"%")


# create labels for display box
labelDisplay = Label(root, textvariable=textDisplay, font=("Arial", 28), borderwidth="2", relief="sunken", anchor="e")
# add white color to background of label
labelDisplay.config(bg="white")

# create button widgets for calculator, need to add commands later
# numerical buttons
buttonOne = Button(root, text="1", font=("Arial", 20), relief="ridge", command=lambda: number("1"))
buttonTwo = Button(root, text="2", font=("Arial", 20), relief="ridge", command=lambda: number("2"))
buttonThree = Button(root, text="3", font=("Arial", 20), relief="ridge", command=lambda: number("3"))
buttonFour = Button(root, text="4", font=("Arial", 20), relief="ridge", command=lambda: number("4"))
buttonFive = Button(root, text="5", font=("Arial", 20), relief="ridge", command=lambda: number("5"))
buttonSix = Button(root, text="6", font=("Arial", 20), relief="ridge", command=lambda: number("6"))
buttonSeven = Button(root, text="7", font=("Arial", 20), relief="ridge", command=lambda: number("7"))
buttonEight = Button(root, text="8", font=("Arial", 20), relief="ridge", command=lambda: number("8"))
buttonNine = Button(root, text="9", font=("Arial", 20), relief="ridge", command=lambda: number("9"))
buttonZero = Button(root, text="0", font=("Arial",20), relief="ridge", command=lambda: number("0"))
buttonDecimal = Button(root, text=".", font=("Arial", 20), relief="ridge", command=lambda: number("."))
# operator buttons
buttonAdd = Button(root, text="+", font=("Arial", 20), relief="ridge", command=addition)
buttonSubtract = Button(root, text="-", font=("Arial", 20), relief="ridge", command=subtraction)
buttonMultiply = Button(root, text="X", font=("Arial", 20), relief="ridge", command=multiply)
buttonDivide = Button(root, text=chr(247), font=("Arial", 26), relief="ridge", command=divide)
buttonClear = Button(root, text="Clear", font=("Arial", 20), relief="ridge", command=clearDisplay)
buttonPercentage = Button(root, text="%", font=("Arial", 20), relief="ridge", command=percentage)
buttonPlusMinus = Button(root, text="+/-", font=("Arial", 20), relief="ridge", command=negative)
buttonEqual = Button(root, text="=", font=("Arial", 20), relief="ridge", command=equal)

# place label on GUI
labelDisplay.place(x=10, y=5, height=70, width=380)

# place buttons on GUI
# column 1
buttonPercentage.place(x=14, y=25+60, height=88, width=95)
buttonSeven.place(x=14, y=25+60+86, height=88, width=95)
buttonFour.place(x=14, y=25+60+86+86, height=88, width=95)
buttonOne.place(x=14, y=25+60+86+86+86, height=88, width=95)
buttonPlusMinus.place(x=14, y=25+60+86+86+86+86, height=88, width=95)
# column 2
buttonClear.place(x=14+93, y=25+60, height=88, width=188)
buttonEight.place(x=14+93, y=25+60+86, height=88, width=95)
buttonFive.place(x=14+93, y=25+60+86+86, height=88, width=95)
buttonTwo.place(x=14+93, y=25+60+86+86+86, height=88, width=95)
buttonZero.place(x=14+93, y=25+60+86+86+86+86, height=88, width=95)
# column 3
buttonNine.place(x=14+93+93, y=25+60+86, height=88, width=95)
buttonSix.place(x=14+93+93, y=25+60+86+86, height=88, width=95)
buttonThree.place(x=14+93+93, y=25+60+86+86+86, height=88, width=95)
buttonDecimal.place(x=14+93+93, y=25+60+86+86+86+86, height=88, width=95)
# column 4
buttonDivide.place(x=14+93+93+93, y=25+60, height=88, width=95)
buttonMultiply.place(x=14+93+93+93, y=25+60+86, height=88, width=95)
buttonSubtract.place(x=14+93+93+93, y=25+60+86+86, height=88, width=95)
buttonAdd.place(x=14+93+93+93, y=25+60+86+86+86, height=88, width=95)
buttonEqual.place(x=14+93+93+93, y=25+60+86+86+86+86, height=88, width=95)

# call the mainloop
root.mainloop()
