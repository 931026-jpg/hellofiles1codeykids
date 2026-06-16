
import turtle

screen = turtle.Screen()
screen.tracer(0)  # Turn off automatic drawing for better performance
t = turtle.Turtle()
score = 0
is_running = True


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

while is_running:
    screen.update()  # Draw
    turtle.delay(100)  # Small delay to control game speed

    if (t.xcor() > 200 or t.xcor() < -200) or (t.ycor() > 200 or t.ycor() < -200):
        print("Game Over! Turtle moved out of bounds. Score:", score)
        is_running = False

turtle.done()

