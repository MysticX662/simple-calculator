from tkinter import *

# Create a window
window = Tk()

# Set the window title
window.title("Calculator")

# Create an entry widget to display the input and output
entry = Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add a number to the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, END)

# Create buttons for numbers and operators
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)

# Place buttons on the window
button_clear.grid(row=1, column=0, columnspan=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_0.grid(row=5, column=0, columnspan=2)
# Function to perform addition
def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to perform subtraction
def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to perform multiplication
def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to perform division
def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to perform equal operation
def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math == "division":
        entry.insert(0, f_num / int(second_number))

# Create operator buttons
button_add = Button(window, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)

# Place operator buttons on the window
button_add.grid(row=5, column=3)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_equal.grid(row=5, column=1, columnspan=2)
# Create number buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Place number buttons on the window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

window.mainloop()