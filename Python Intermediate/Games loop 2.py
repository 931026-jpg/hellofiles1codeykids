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
count = 0
def handle_click(x, y):
    global count
    count += 1 # Update count
    draw() # Pass control to draw
def draw():
    t.clear()
    t.write(f"Count: {count}", align="center", font=("Arial", 50,
"normal"))
screen.onclick(handle_click) # Listens for left-click then passes
##control to handle_click
draw()
turtle.done() # Start the game here

def handle_right_click(x, y):
    # do stuff
    screen.onclick(handle_right_click, btn=3) # Right click is button 

screen = turtle.Screen()
t = turtle.Turtle()
count = 0
def update():
    global count
    count += 1 # Update count

screen.ontimer(update, 1000) # call update after 1 second
draw() # Pass control to draw
def draw():
    t.clear()
t.write(f"Count: {count}", align="center", font=("Arial", 50,
"normal"))
screen.ontimer(update, 1000) # call update after 1 second
draw()
turtle.done() # Start the game here






#Started
def update():
    global count
count += 1   
if not is_running:
return
screen.ontimer(update, 1000)   
draw()     
def game_over():
    t.clear()
t.write("Game Over", align="center", font=("Arial", 50, "normal"))
