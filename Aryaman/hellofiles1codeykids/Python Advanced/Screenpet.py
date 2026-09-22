'''
Project: Screen Pet
Author:
Date

[This]

'''

'''
TODO:
1. Copy over your screen pet drawing here to animate it! (Or you can make a new one if you wish)
2. Decide on at least 3 events and their corresponding actions
    EXAMPLES
    - Draw a set of closed eyes, and opened eyes. Pet blinks automatically. Pet winks if eyes clicked.
    - Draw an exaggerated smile. Pet switched mouth to smile if user moves mouse over face.
    - On activation (when window is created) Pet smiles / Any action
    - A pet's feature (ex. nose, ears) changes colour when clicked
'''

'''
HOW TO CREATE ALTERNATE VERSIONS:
1. Create a variable storing version 1, set state to NORMAL
2. Create a variable storing version 2, set state to HIDDEN
    This will create the object, but not place it on the screen.

HOW TO SWITCH BETWEEN THE VERSION:
1. Create a function that toggles
    1.1. Figure out which version is currently in use
        - do this using a global variable that keeps track of this OR
        - fetch the current state of the canvas object involved ex. if the variable for verson 1's state is HIDDEN (using c.itemcget function)
    1.2  Switch the state for the version in use to HIDDEN
    1.3  Switch the state for the other version to NORMAL - if using a global variable, change it now
2. Ensure this function is bound to the appropriate event
(EXAMPLE GIVEN - crossed and uncrossed version of eyes)

'''

'''
HOW TO MAKE ACTIONS OCCUR AUTOMATICALLY - TIMED
If you want func_a function to happen every second, in the function definition, write
root.after(1000, func_a) <- this tells the root to call this function again after 1000 milliseconds
Ensure function is called once in the main code.
(EXAMPLE GIVEN - crossing and uncrossing eyes is done automatically)

'''


from tkinter import *
root = Tk()

c = Canvas(root, width=500, height=500, bg='light blue')
crossed = False  # Starting out with uncrossed eyes


def toggle_eyes():
    '''
    If using a global variable, include lines like this to 
    use and check that variable

    global crossed
    if not crossed:
    '''
    # This function uses the approach of checking an object's state to determine what version is currently used
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)
        '''crossed = True # this is ESSENTIAL if using the global variable approach'''

    else:
        c.itemconfigure(left_eye_pupil_2, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_2, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_1, state=NORMAL)
        c.itemconfigure(right_eye_pupil_1, state=NORMAL)
        '''crossed = False'''

    # after 1000 milliseconds, call this function again
    root.after(1000, toggle_eyes)


left_eye_white = c.create_oval(100, 100, 120, 120, fill='white', tags=('eye'))
right_eye_white = c.create_oval(150, 100, 170, 120, fill='white', tags=('eye'))

# Normal pupils - the tags here haven't been used in this example but they may be helpful for other events
left_eye_pupil_1 = c.create_oval(105, 105, 115, 115, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)
right_eye_pupil_1 = c.create_oval(155, 105, 165, 115, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)

# Crossed eye pupils
left_eye_pupil_2 = c.create_oval(107, 107, 117, 117, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)
right_eye_pupil_2 = c.create_oval(153, 103, 163, 113, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)

toggle_eyes()  # function must be called once in the main code to start the automatic process


c.pack()
root.mainloop()
