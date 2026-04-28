import tkinter as tk
from functools import reduce
import operator as op
import re


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
    
    parts = re.split(r'(\+|-|\*|/)', entry.get())  # splits the input into numbers and operators
    print(parts)
    result = parts[0]  # first number
    for i in range(1, len(parts), 2):
        operator = parts[i]
        num = int(parts[i + 1])
        if operator == '+':
            result = int(result) + num
        elif operator == '-':
            result = int(result) - num
        elif operator == '*':
            result = int(result) * num
        elif operator == '/':
            result = int(result) / num
    # applies the operator to the result and the next number
    print(parts)
    
    result_label.config(text="Result: " + str(result))


button = tk.Button(root, text="submit", command=print_input) # button for printing inputs and results
button.pack(pady=10)


root.mainloop()