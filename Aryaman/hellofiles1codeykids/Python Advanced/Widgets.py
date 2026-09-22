'''
Project Title:Wigets
Author: Aryaman Singh
Date: July 28th 2026.

[Making on screen widets using tkinter to help improve and enhance the user experience with sharpening my mind and coding skills while having fun and learning new things]

'''
'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''





from tkinter import *

root = Tk()
root.title(" Turtle Quizzzzzzz")
root.geometry("550x750")
root.configure(bg="#28292E") 

stringvars = []
answers = []
result = StringVar()

def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(f"You scored: {points} / {len(answers)}")

bg_col = "#848fa1"
fg_col = "#ffffff"
frame_pad = 10
lbl_font = ("Arial", 11, "bold")
title_label = Label(root, text="🐍 🐢 Quiz", font=("Arial", 16, "bold"), bg="#2b2d42", fg="#edf2f4")
title_label.pack(pady=15)

# Question 1
q1_var = StringVar()
stringvars.append(q1_var)
answers.append("turtle.forward(100)")

f1 = Frame(root, bg=bg_col, padx=frame_pad, pady=frame_pad, bd=3, relief=RAISED)
f1.pack(fill=X, padx=20, pady=8)

Label(f1, text="1. What turtle command moves it forward by 100 pixels?", bg=bg_col, fg=fg_col, font=lbl_font).pack(anchor=W)
Entry(f1, textvariable=q1_var, width=30, font=("Courier", 10)).pack(anchor=W, pady=(5,0))

# Question 2:
q2_var = StringVar()
q2_var.set("None")
stringvars.append(q2_var)
answers.append("t = turtle.Turtle()")
f2 = Frame(root, bg=bg_col, padx=frame_pad, pady=frame_pad, bd=3, relief=RAISED)
f2.pack(fill=X, padx=20, pady=8)
Label(f2, text="2. Which line of code creates a new turtle object?", bg=bg_col, fg=fg_col, font=lbl_font).pack(anchor=W)

options = ["t = turtle.Turtle()", "t = new Turtle", "create(turtle)"]
for opt in options:
    Radiobutton(f2, text=opt, variable=q2_var, value=opt, bg=bg_col, activebackground=bg_col, font=("Courier", 10)).pack(anchor=W)

# Question 3
q3_var = StringVar()
q3_var.set("Select an option...")
stringvars.append(q3_var)
answers.append("Stops the turtle from drawing")

f3 = Frame(root, bg=bg_col, padx=frame_pad, pady=frame_pad, bd=3, relief=RAISED)
f3.pack(fill=X, padx=20, pady=8)
Label(f3, text="3. What does the penup() command do?", bg=bg_col, fg=fg_col, font=lbl_font).pack(anchor=W)
OptionMenu(f3, q3_var, "Makes the turtle jump", "Stops the turtle from drawing", "Erases the screen").pack(anchor=W, pady=(5,0))
 
# Question 4: Checkbutton Widget
q4_var = StringVar()
q4_var.set("False") # Default state
stringvars.append(q4_var)
answers.append("True")

f4 = Frame(root, bg=bg_col, padx=frame_pad, pady=frame_pad, bd=3, relief=RAISED)
f4.pack(fill=X, padx=20, pady=8)

Label(f4, text="4. True or False: 'turtle' is a built-in Python module.", bg=bg_col, fg=fg_col, font=lbl_font).pack(anchor=W)
Checkbutton(f4, text="Check this box if TRUE", variable=q4_var, onvalue="True", offvalue="False", bg=bg_col, activebackground=bg_col).pack(anchor=W)

# Question 5: Spinbox Widget
q5_var = StringVar()
q5_var.set("0")
stringvars.append(q5_var)
answers.append("90")

f5 = Frame(root, bg=bg_col, padx=frame_pad, pady=frame_pad, bd=3, relief=RAISED)
f5.pack(fill=X, padx=20, pady=8)

Label(f5, text="5. To draw a square, what angle goes in the right() command?", bg=bg_col, fg=fg_col, font=lbl_font).pack(anchor=W)
Spinbox(f5, from_=0, to=360, increment=45, textvariable=q5_var, width=10, font=("Courier", 10)).pack(anchor=W, pady=(5,0))

submitButton = Button(root, text='Submit Answers', bg='#ef233c', fg='white', font=("Arial", 12, "bold"), 
                      padx=20, pady=5, command=check_answers, cursor="hand2")
submitButton.pack(pady=15)

results = Label(root, textvariable=result, font=("Arial", 16, "bold"), bg="#2b2d42", fg="#edf2f4")
results.pack()

root.mainloop()
