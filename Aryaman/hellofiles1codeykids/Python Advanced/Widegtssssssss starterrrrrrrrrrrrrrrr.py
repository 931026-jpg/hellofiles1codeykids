'''
Project Title:Widegttts
Author:jhdasjkfdkjsdafkgvjfdkjdfkdsfakfsdkjfdasgfadsouohgafdslkgafdofdsfaadsdfsadf
Date:

[insert description of project and instructions for use
It said this was optional, '''





from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()


def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here


# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
results = Label(root, textvariable=result)
results.pack()

root.mainloop()