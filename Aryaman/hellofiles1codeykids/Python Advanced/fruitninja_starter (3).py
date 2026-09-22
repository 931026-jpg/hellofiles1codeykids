'''
Project:
Author:
Date:
[insert a description of your project and how to play!]
'''

# Imports go here, you'll need tkinter and some functions from the random module

# Create your window and call it 'root'
# Create your Canvas and call it 'c'

class Fruit():
    '''
    Fruit will be the parent class for Watermelon, Banana, and Coconut (+ any other fruits you add)
    Inside this class, write the __init__ function, which will be EXTREMELY similar to the __init__ of the Bug
    class as shown in the worksheet.

    At the bottom of the __init__ function add either the line
    'c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)' OR
    'c.tag_bind(self.obj, '<Motion>', self.destroy)'
    The first will make it so that clicking a fruit will eliminate it, the second
    will make it so that moving the mouse over the fruit will eliminate it.
    Choose whichever method would make the game more fun for you!
    
    Then, as the last line of the __init__,  add the line:
     'self.move()'
    This will ensure the fruit starts falling as soon as it is created
    '''
    
    # Put __init__ function here

    def destroy(self, event):
        c.delete(self.obj)

    def move(self):
        '''
        This function allows the fruits to fall down the screen.
        '''
        # the canvas is told to move this fruit's Canvas Object 0 units right and 1 unit down
        # change the 0 to a nonzero value to have the fruit move left or right
        # change the 1 to a higher number for it to fall faster
        c.move(self.obj, 0, 1)

        # after 100 milliseconds, the root will call this function again
        # this way, the fruits keep on falling all the time
        # change the 100 to make the fruit fall faster or slower, but
        # it may look a little choppy
        root.after(100, self.move)

# Create your other fruit classes here - as CHILDREN of the Fruit class
# Their __init__ functions should be VERY SIMPLE
# Each of your fruit classes should have nearly identical, VERY SIMPLE code


'''
Create your Bomb class here.
The __init__ should
- create the bomb's Canvas Object and store it as an instance variable
- copy the given extra lines from the Fruit class comments
Give it a destroy method, but it should instead just
print out 'YOU HIT A BOMB', then quit the game using
'root.quit()' which closes our window.
Copy the move function from Fruit here too since it should also fall down the screen.
'''

""" CHALLENGE """
# The Bomb class and Fruit class have very very similar code!
# Perhaps this is a sign that the hierarchy could be done better?
# As an extra challenge, see if you can make a more efficient hierarchy
# - Should Bomb be a child of Fruit?
# - Should Bomb and Fruit be a child of some other class, like a FallingObject class?