import tkinter as tk
from functools import reduce
import operator as op


root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.pack()  

# Operator functions
def dif(numbers):
    return reduce(op.sub, numbers)

def mul(numbers):
    return reduce(op.mul, numbers)

def div(numbers):
    return reduce(op.truediv, numbers)


# Input
def print_input():
    label = tk.Label(root, text="Input: " + entry.get())
    label.pack()

    if "+" in entry.get():
        parts = entry.get().split("+")  # split the input by the + operator
        operator = "+"                  # set the operator for later
    elif "-" in entry.get():
        parts = entry.get().split("-")
        operator = "-"
    elif "*" in entry.get():
        parts = entry.get().split("*")
        operator = "*"
    elif "/" in entry.get():
        parts = entry.get().split("/")
        operator = "/"
    else:
        result_label.config(text="No valid operator found.")
        return
    
    numbers = []
    for part in parts:                  # each part of the input is converted to an integer
        numbers.append(int(part))
    
    if operator == "+":                 # if the operator is +, adds the numbers together
        result = sum(numbers) 
        result_label.config(text="Result: " + str(result))
    
    if operator == "-":
        result = dif(numbers)
        result_label.config(text="Result: " + str(result))

    if operator == "*":
        result = mul(numbers)
        result_label.config(text="Result: " + str(result))

    if operator == "/":
        result = div(numbers)
        result_label.config(text="Result: " + str(result))


button = tk.Button(root, text="submit", command=print_input) # button for printing inputs
button.pack(pady=10)


root.mainloop()