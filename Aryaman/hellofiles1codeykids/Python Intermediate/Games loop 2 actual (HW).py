import turtle
import time

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Man Hunt: Red vs Blue")
screen.setup(800, 600)
screen.bgcolor("black")

# Turn off automatic updates
screen.tracer(0)

# --- Create turtles ---

# Blue turtle (player 1)
blue = turtle.Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(-200, 0)

# Red turtle (player 2)
red = turtle.Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(200, 0)

# Timer turtle
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.color("white")
timer_turtle.penup()
timer_turtle.goto(0, 260)

# --- Game state ---
time_left = 60

# --- Movement handlers (blue: WASD) ---

MOVE_STEP = 20

def blue_up():
    y = blue.ycor() + MOVE_STEP
    blue.sety(y)
    screen.update()

def blue_down():
    y = blue.ycor() - MOVE_STEP
    blue.sety(y)
    screen.update()

def blue_left():
    x = blue.xcor() - MOVE_STEP
    blue.setx(x)
    screen.update()

def blue_right():
    x = blue.xcor() + MOVE_STEP
    blue.setx(x)
    screen.update()

# --- Movement handlers (red: arrow keys) ---

def red_up():
    y = red.ycor() + MOVE_STEP
    red.sety(y)
    screen.update()

def red_down():
    y = red.ycor() - MOVE_STEP
    red.sety(y)
    screen.update()

def red_left():
    x = red.xcor() - MOVE_STEP
    red.setx(x)
    screen.update()

def red_right():
    x = red.xcor() + MOVE_STEP
    red.setx(x)
    screen.update()

# --- Timer handler ---

def draw_time():
    timer_turtle.clear()
    timer_turtle.write(f"Time left: {time_left}", align="center",
                       font=("Arial", 24, "bold"))

def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        draw_time()
        screen.update()
        screen.ontimer(timer, 1000)

# --- Key bindings ---

screen.listen()

# Blue: WASD
screen.onkeypress(blue_up, "w")
screen.onkeypress(blue_left, "a")
screen.onkeypress(blue_down, "s")
screen.onkeypress(blue_right, "d")

# Red: arrows
screen.onkeypress(red_up, "Up")
screen.onkeypress(red_left, "Left")
screen.onkeypress(red_down, "Down")
screen.onkeypress(red_right, "Right")

# --- Start timer ---
draw_time()
screen.update()
screen.ontimer(timer, 1000)

# --- Game loop: collision + win logic ---

game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.color("white")
game_over_turtle.penup()
game_over_turtle.goto(0, 0)

while time_left > 0:
    screen.update()
    # Check collision
    if blue.distance(red) < 20:
        game_over_turtle.write("Red wins! (Caught blue!)", align="center",
                               font=("Arial", 28, "bold"))
        break
    time.sleep(0.01)

# If loop ended because time ran out
if time_left <= 0 and blue.distance(red) >= 20:
    game_over_turtle.write("Blue wins! (Time's up!)", align="center",
                           font=("Arial", 28, "bold"))

# Stop timer
time_left = 0

turtle.done()