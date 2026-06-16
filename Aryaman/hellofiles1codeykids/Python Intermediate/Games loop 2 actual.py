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
screen = turtle.Screen()
t = turtle.Turtle()
screen.tracer(0)  # Turn off automatic drawing for better performance
score = 0
is_running = True
t.shape('turtle')


def update():
    """Updates the counter and redraws the screen every second."""
    global score
    score += 2.5
    if not is_running:
        return
  
    screen.ontimer(update, 2500)
    draw()

def game_over():
    """Displays the game over message."""
    global is_running
    is_running = False
    
    t.clear()
    t.write("Game Over", align="center", font=("Arial", 50, "normal"))

    
def draw():
    """Example draw function — replace with your own drawing logic."""
    t.clear()
    t.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))




# Global variables
#count = 0
#s_running = True


def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)



screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey( game_over,"q")
##while is_running:
##    screen.update()  # Draw

screen.ontimer(update, 2500)  
draw()

turtle.done()

