import turtle
import random

# -----------------------------
# CONFIG
# -----------------------------
ROWS = 17
COLS = 25
MINES = 85
0
CELL = 30

COLORS = {
    1: "blue",
    2: "green",
    3: "red",
    4: "darkblue",
    5: "brown",
    6: "turquoise",
    7: "black",
    8: "gray"
}

# -----------------------------
# SCREEN SETUP
# -----------------------------
screen = turtle.Screen()
screen.title("Mineswooped")
screen.setup(COLS * CELL + 200, ROWS * CELL + 200)
screen.bgcolor("lightgray")
screen.tracer(0)   # fast mode

# -----------------------------
# TURTLES
# -----------------------------
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("black")

reset_turtle = turtle.Turtle()
reset_turtle.hideturtle()
reset_turtle.penup()
reset_turtle.speed(0)

# -----------------------------
# GAME STATE
# -----------------------------
revealed = [[False]*COLS for _ in range(ROWS)]
flagged = [[False]*COLS for _ in range(ROWS)]
mines = [[False]*COLS for _ in range(ROWS)]
first_click = True
game_over = False

time_left = 999
mine_count = MINES

# Reset button state
reset_x = 0
reset_y = (ROWS * CELL) // 2 + 60
reset_size = 40

# -----------------------------
# DRAWING HELPERS
# -----------------------------
def cell_to_xy(r, c):
    x = c * CELL - (COLS * CELL)//2
    y = (ROWS * CELL)//2 - r * CELL
    return x, y

def draw_cell(r, c):
    x, y = cell_to_xy(r, c)
    drawer.goto(x, y)
    drawer.pendown()

    # Hidden cell
    if not revealed[r][c]:
        drawer.color("yellow" if flagged[r][c] else "darkgreen")
        drawer.begin_fill()
        for _ in range(4):
            drawer.forward(CELL)
            drawer.right(90)
        drawer.end_fill()
        drawer.penup()
        return

    # Revealed mine
    if mines[r][c]:
        drawer.color("red")
        drawer.begin_fill()
        for _ in range(4):
            drawer.forward(CELL)
            drawer.right(90)
        drawer.end_fill()
        drawer.penup()
        return

    # Revealed empty cell
    drawer.color("white")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

    count = adjacent_mines(r, c)
    if count > 0:
        drawer.goto(x + CELL//2, y - CELL + 5)
        drawer.color(COLORS[count])
        drawer.write(str(count), align="center", font=("Arial", 16, "bold"))

def draw_grid():
    drawer.clear()
    for r in range(ROWS):
        for c in range(COLS):
            draw_cell(r, c)
    screen.update()

def draw_reset_button():
    reset_turtle.clear()
    reset_turtle.goto(reset_x - reset_size//2, reset_y - reset_size//2)
    reset_turtle.pendown()
    reset_turtle.color("yellow")
    reset_turtle.begin_fill()
    for _ in range(4):
        reset_turtle.forward(reset_size)
        reset_turtle.right(90)
    reset_turtle.end_fill()
    reset_turtle.penup()

    reset_turtle.goto(reset_x, reset_y - 10)
    reset_turtle.color("black")
    reset_turtle.write("☺", align="center", font=("Arial", 28, "bold"))
    screen.update()

# -----------------------------
# MINE LOGIC
# -----------------------------
def place_mines(safe_r, safe_c):
    placed = 0
    safe_zone = {(safe_r + dr, safe_c + dc)
                 for dr in (-1, 0, 1)
                 for dc in (-1, 0, 1)
                 if 0 <= safe_r + dr < ROWS and 0 <= safe_c + dc < COLS}

    while placed < MINES:
        r = random.randint(0, ROWS-1)
        c = random.randint(0, COLS-1)
        if (r, c) not in safe_zone and not mines[r][c]:
            mines[r][c] = True
            placed += 1

def adjacent_mines(r, c):
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            nr, nc = r+dr, c+dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if mines[nr][nc]:
                    count += 1
    return count

# -----------------------------
# REVEAL LOGIC
# -----------------------------
def flood_fill(r, c):
    if not (0 <= r < ROWS and 0 <= c < COLS):
        return
    if revealed[r][c] or flagged[r][c]:
        return

    revealed[r][c] = True

    if adjacent_mines(r, c) == 0:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    flood_fill(r+dr, c+dc)

def reveal(r, c):
    global game_over, first_click

    if game_over:
        return
    if flagged[r][c]:
        return

    if first_click:
        place_mines(r, c)
        first_click = False

    revealed[r][c] = True

    if mines[r][c]:
        game_over = True
        reveal_all_mines()
        show_message("Game Over — You hit a mine")
        return

    if adjacent_mines(r, c) == 0:
        flood_fill(r, c)

def reveal_all_mines():
    for r in range(ROWS):
        for c in range(COLS):
            if mines[r][c]:
                revealed[r][c] = True


# UI TEXT
def show_message(msg):
    text.clear()
    text.goto(0, - (ROWS*CELL)//2 - 40)
    text.write(msg, align="center", font=("Arial", 20, "bold"))
    screen.update()

def draw_header():
    text.clear()
    text.goto(0, (ROWS*CELL)//2 + 20)
    text.write(f"Mines: {mine_count}   Time: {time_left}",
               align="center", font=("Arial", 18, "bold"))
    screen.update()

# TIMER
def timer_tick():
    global time_left
    if game_over:
        return
    if time_left > 0:
        time_left -= 1
        draw_header()
        screen.ontimer(timer_tick, 1000)

# RESET GAME
def reset_game():
    global revealed, flagged, mines, first_click, game_over
    global time_left, mine_count

    revealed = [[False]*COLS for _ in range(ROWS)]
    flagged = [[False]*COLS for _ in range(ROWS)]
    mines = [[False]*COLS for _ in range(ROWS)]

    first_click = True
    game_over = False
    time_left = 999
    mine_count = MINES

    text.clear()
    draw_header()
    draw_grid()
    draw_reset_button()

# INPUT HANDLERS
def left_click(x, y):
    global game_over

    # Check reset button click
    if (reset_x - reset_size//2 <= x <= reset_x + reset_size//2 and
        reset_y - reset_size//2 <= y <= reset_y + reset_size//2):
        reset_game()
        return

    if game_over:
        return

    c = int((x + (COLS*CELL)//2) // CELL)
    r = int(((ROWS*CELL)//2 - y) // CELL)

    if 0 <= r < ROWS and 0 <= c < COLS:
        reveal(r, c)
        draw_grid()
        draw_header()
        check_win()

def right_click(x, y):
    global mine_count
    if game_over or first_click:
        return

    c = int((x + (COLS*CELL)//2) // CELL)
    r = int(((ROWS*CELL)//2 - y) // CELL)

    if 0 <= r < ROWS and 0 <= c < COLS:
        if not revealed[r][c]:
            flagged[r][c] = not flagged[r][c]
            mine_count += -1 if flagged[r][c] else 1
            draw_grid()
            draw_header()

# WIN CHECK
def check_win():
    global game_over
    for r in range(ROWS):
        for c in range(COLS):
            if not mines[r][c] and not revealed[r][c]:
                return
    show_message("You Win!")
    game_over = True

# BIND EVENTS
screen.onclick(left_click)
screen.onscreenclick(right_click, btn=3)

# START GAME
draw_grid()
draw_header()
draw_reset_button()
timer_tick()

turtle.done()
