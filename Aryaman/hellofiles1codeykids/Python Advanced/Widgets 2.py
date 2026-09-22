import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Survey")
#good oneee iutewouqorqwerqehiureihrq
# Name
ttk.Label(root, text="Full Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Birthdate
ttk.Label(root, text="Birthdate:").grid(row=1, column=0, padx=5, pady=5)
day = ttk.Combobox(root, values=list(range(1, 32)), width=5)
month = ttk.Combobox(root, values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], width=5)
year = ttk.Combobox(root, values=list(range(1900, 2026)), width=7)
day.grid(row=1, column=1)
month.grid(row=1, column=2)
year.grid(row=1, column=3)

# Phone Number
ttk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=5, pady=5)
phone_entry = ttk.Entry(root)
phone_entry.grid(row=2, column=1, padx=5, pady=5)
# Submit button
def submit():
    messagebox.showinfo("Survey Complete", "Thank you for answering my good survey 🙃🙃🙃🙃🙃🙃🙃🙃")

ttk.Button(root, text="Enter", command=submit).grid(row=3, column=1, pady=10)




root.mainloop()

 
 
 
 
 
 
 
"""  
 #Bad copy 1
 
import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Very great #1")

# Name (user must pick a color, and the color name becomes their name)
def pick_name():
    color = colorchooser.askcolor()[1]
    print("Your name is:", color)

tk.Button(root, text="Choose Your Name (as a color)").pack()

# Birthdate (user must pick a number between 1 and 10,000)
tk.Label(root, text="Birthdate (pick a number 1–10000):").pack()
birth_spin = tk.Spinbox(root, from_=1, to=10000)
birth_spin.pack()

# Phone number (scale from 0 to 9,999,999,999)
tk.Label(root, text="Phone Number:").pack()
phone_scale = tk.Scale(root, from_=0, to=9999999999, orient="horizontal", length=800)
phone_scale.pack()

root.mainloop()


 """






""" 

#Bad copy 2 the sequel


import tkinter as tk
import random

root = tk.Tk()
root.title("Very great 2 #2")

# Name (user must type backwards; entry hides text)
tk.Label(root, text="Enter your name BACKWARDS:").pack()
name_entry = tk.Entry(root, show="*")
name_entry.pack()

# Birthdate (sliders that move each other)
def chaos(event):
    month_slider.set(random.randint(1,12))
    day_slider.set(random.randint(1,31))

tk.Label(root, text="Birth Month:").pack()
month_slider = tk.Scale(root, from_=1, to=12, orient="horizontal")
month_slider.pack()

tk.Label(root, text="Birth Day:").pack()
day_slider = tk.Scale(root, from_=1, to=31, orient="horizontal")
day_slider.pack()

month_slider.bind("<Motion>", chaos)

# Phone number (digits appear randomly)
tk.Label(root, text="Click digits to enter phone number:").pack()
phone = ""

def spawn_digit():
    digit = str(random.randint(0,9))
    btn = tk.Button(root, text=digit, command=lambda d=digit: print("Pressed:", d))
    btn.place(x=random.randint(0,300), y=random.randint(0,300))
    root.after(1000, spawn_digit)

spawn_digit()

root.mainloop()
 """