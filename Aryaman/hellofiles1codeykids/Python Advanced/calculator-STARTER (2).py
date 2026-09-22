'''
Calculator Builder
Author: Aryaman Singh
Date:

[This will be a very elegant recreeation of a calucaulator using the tkinter library.Will be using the StringVar class to store the expression and a custom button class to make creating buttons easier.  The calculator will be able to evaluate expressions using the built-in eval function.  The calculator will also have a clear button and a delete button to remove the last character in the expression.]

'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =, DEL (or DELETE or BACKSPACE)
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""


from tkinter import *

root = Tk()
root.title("Calculator")
expression = StringVar()

# ---------------- THEMES ----------------
dark = {"bg":"#222","fg":"white","btn":"#333","eq":"#4CAF50","clr":"#D32F2F"}
light = {"bg":"#EEE","fg":"black","btn":"#DDD","eq":"#4CAF50","clr":"#D32F2F"}
theme = dark

def apply_theme():
    root.configure(bg=theme["bg"])
    display.configure(bg="white" if theme==light else "#555", fg=theme["fg"])
    for b in buttons: b.obj.configure(bg=theme["btn"], fg=theme["fg"])
    eq_btn.obj.configure(bg=theme["eq"], fg="white")
    clr_btn.obj.configure(bg=theme["clr"], fg="white")
    toggle.configure(bg=theme["btn"], fg=theme["fg"])

def toggle_theme():
    global theme
    theme = light if theme == dark else dark
    apply_theme()

# ---------------- BUTTON CLASS ----------------
class CalcButton:
    def __init__(self, char, r, c, w=1):
        self.char = char
        self.obj = Button(root, text=char, font=("Arial",18),
                          command=self.onClick)
        self.obj.grid(row=r, column=c, columnspan=w,
                      sticky="nsew", padx=5, pady=5)

    def onClick(self):
        # Convert pretty symbols to Python operators
        if self.char == "×":
            expression.set(expression.get() + "*")
        elif self.char == "÷":
            expression.set(expression.get() + "/")
        else:
            expression.set(expression.get() + self.char)

# ---------------- FUNCTIONS ----------------
def clear():
    expression.set('')

def delete():
    expression.set(expression.get()[:-1])

def evaluate():
    try:
        expression.set(str(eval(expression.get().strip())))
    except:
        expression.set("Error")

# ---------------- DISPLAY ----------------
display = Entry(root, textvariable=expression,
                font=("Arial",24), justify="right", bd=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4,
             sticky="nsew", padx=10, pady=10)

# ---------------- BUTTONS ----------------
buttons = []

layout = [
    ("7",1,0),("8",1,1),("9",1,2),("÷",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("×",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,3)
]

for char,r,c in layout:
    buttons.append(CalcButton(char,r,c))

# Equal button
eq_btn = CalcButton("=",4,2)
eq_btn.obj.configure(command=evaluate)

# Clear button
clr_btn = CalcButton("CLEAR",5,0,4)
clr_btn.obj.configure(command=clear)

# Delete button
del_btn = CalcButton("DEL",6,0,2)
del_btn.obj.configure(command=delete)

# Theme toggle
toggle = Button(root, text="Toggle Theme", font=("Arial",14),
                command=toggle_theme)
toggle.grid(row=6, column=2, columnspan=2,
            sticky="nsew", padx=10, pady=10)

# ---------------- GRID CONFIG ----------------
for i in range(7): root.rowconfigure(i, weight=1)
for i in range(4): root.columnconfigure(i, weight=1)

apply_theme()
root.mainloop()
