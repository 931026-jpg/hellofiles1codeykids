'''


Project Name: Tkinter
Author:Aryaman
Date: June 16th 2026

This is a title block! Title blocks help you keep track of the purpose and 
progress of a project. We will be including one at the beginning of all projects
from now on.

After filling out the 3 pieces of information, write a short blurb on 
what this project does and how to use it! This only needs to be two sentences
for this simple project.
'''
'''


TODO:
- create a canvas with a
    - background colour
    - size

- using lines, polygons, rectangles, and ovals, draw an animal on your canvas
- tag all your canvas objects!
'''




from tkinter import *
def print_loc(event):
    '''
    This function is made for you to help you get familiar with the grid on the
    screen!

    It will print out the X, Y coordinates of any point you want.
    When your program is running, simply click (using left moust button)
    on the point on the canvas you want the location of.
    The output will be in the shell!

    '''
    print(event.x, event.y)


# Your window has been made for you below
root = Tk()

# this line allows our print function to be called when and wherever you click
root.bind("<Button-1>", print_loc)

# Create your canvas and all your canvas objects here! Don't forget to pack!














root.mainloop()
