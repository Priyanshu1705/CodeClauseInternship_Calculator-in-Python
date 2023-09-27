import tkinter as tk
from tkinter import messagebox

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        messagebox.showerror("Error", "Cannot divide by zero")

def power(num1, num2):
    return num1 ** num2

def square_root(num):
    if num >= 0:
        return num ** 0.5
    else:
        messagebox.showerror("Error", "Cannot calculate square root of a negative number")

def factorial(num):
    if num >= 0:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    else:
        messagebox.showerror("Error", "Cannot calculate factorial of a negative number")

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = choice_var.get()

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = power(num1, num2)
        elif choice == 6:
            result = square_root(num1)
        elif choice == 7:
            result = factorial(num1)
        # Add more conditions here...

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the GUI
window = tk.Tk()
window.title("Calculator")

# Create input fields
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create choice variable
choice_var = tk.IntVar()

# Create radio buttons for operation selection
choices = [
    ("Add", 1),
    ("Subtract", 2),
    ("Multiply", 3),
    ("Divide", 4),
    ("Power", 5),
    ("Square Root", 6),
    ("Factorial", 7)
    # Add more options here...
]

for text, choice in choices:
    radio_button = tk.Radiobutton(window, text=text, variable=choice_var, value=choice)
    radio_button.pack()

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# Create result field
entry_result = tk.Entry(window)
entry_result.pack()

# Run the GUI
window.mainloop()