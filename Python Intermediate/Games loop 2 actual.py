### this is one way to open a file,
##with open('review.txt') as f:
##    content = f.read() # what type is content?
##print(content) # what would this print?
##f.seek(0) # go back to the beginning of the file
##lines = f.readlines() # what type is lines?
##print(lines) # what would this print?
##f.seek(0) # go back to the beginning of the file
##line = f.readline() # what type is line?
##print(line) # what would this print?
##f.write("New line\n") # would this work? why or why not?
##

import turtle

# Global variables
count = 0
is_running = True

# Create turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

def draw():
    """Example draw function — replace with your own drawing logic."""
    t.clear()
    t.write(f"Count: {count}", align="center", font=("Arial", 24, "normal"))

def update():
    """Updates the counter and redraws the screen every second."""
    global count, is_running
    count += 1

    if not is_running:
        return

    draw()
    screen.ontimer(update, 1000)  

def game_over():
    """Displays the game over message."""
    global is_running
    is_running = False
    t.clear()
    t.write("Game Over", align="center", font=("Arial", 50, "normal"))

# Start the game
draw()
screen.ontimer(update, 1000)
turtle.done()


