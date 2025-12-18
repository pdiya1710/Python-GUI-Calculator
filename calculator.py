# Python Calculator — *GUI Calculator using Tkinter*
# What you learn:** GUI programming, event handling, clean Python structure

import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

# Functions

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# Entry field
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=10, relief="sunken", justify="right")
entry.pack(fill="x", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0
for btn in buttons:
    if btn == '=':
        tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
                  command=lambda b=btn: press(b)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", width=20, height=2, font=("Arial", 12),
          command=clear).pack(pady=10)

root.mainloop()
