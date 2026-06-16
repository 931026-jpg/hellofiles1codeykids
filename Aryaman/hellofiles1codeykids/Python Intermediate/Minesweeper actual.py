import turtle
import random

# Game constants
GRID_SIZE = 20
CELL_SIZE = 30
MINE_COUNT = 100
COLOURS = ["", "blue", "green", "red", "darkblue",
           "brown", "teal", "black", "gray"]

# Initialize screen
screen = turtle.Screen()
screen.title("Minesweeper")
screen.setup(GRID_SIZE * CELL_SIZE + 50, GRID_SIZE * CELL_SIZE + 50)
screen.bgcolor("blue")

# Create turtle for drawing
grid_turtle = turtle.Turtle()
grid_turtle.hideturtle()
grid_turtle.speed(0)
grid_turtle.penup()

# Game state
revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
flags = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
mines = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
game_over = False
first_click = True


def place_mines(click_row, click_col):
    """Place mines randomly, avoiding the first clicked cell and its neighbors"""
    safe_zone = set()
    for r in range(max(0, click_row - 1), min(GRID_SIZE, click_row + 2)):
        for c in range(max(0, click_col - 1), min(GRID_SIZE, click_col + 2)):
            safe_zone.add((r, c))

    mines_placed = 0
    while mines_placed < MINE_COUNT:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if (row, col) not in safe_zone and not mines[row][col]:
            mines[row][col] = True
            mines_placed += 1


def count_adjacent_mines(row, col):
    """Count mines in adjacent cells"""
    count = 0
    for r in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
        for c in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
            if mines[r][c]:
                count += 1
    return count


def draw_cell(row, col):
    """Draw a single cell"""
    x = col * CELL_SIZE - (GRID_SIZE * CELL_SIZE) // 2
    y = (GRID_SIZE * CELL_SIZE) // 2 - row * CELL_SIZE

    grid_turtle.penup()
    grid_turtle.goto(x, y)
    grid_turtle.pendown()

    # Draw revealed cell
    if revealed[row][col]:
        if mines[row][col]:
            grid_turtle.color("red")
            grid_turtle.begin_fill()
            for _ in range(4):
                grid_turtle.forward(CELL_SIZE)
                grid_turtle.right(90)
            grid_turtle.end_fill()
        else:
            grid_turtle.color("black")
            grid_turtle.fillcolor("lightgrey")
            grid_turtle.begin_fill()
            for _ in range(4):
                grid_turtle.forward(CELL_SIZE)
                grid_turtle.right(90)
            grid_turtle.end_fill()

            count = count_adjacent_mines(row, col)
            if count > 0:
                grid_turtle.penup()
                grid_turtle.goto(x + CELL_SIZE // 2, y - CELL_SIZE + 5)
                grid_turtle.color(COLOURS[count])
                grid_turtle.write(str(count), align="center", font=("Arial", 16, "bold"))

    # Draw flagged cell
    elif flags[row][col]:
        grid_turtle.color("green")
        grid_turtle.begin_fill()
        for _ in range(4):
            grid_turtle.forward(CELL_SIZE)
            grid_turtle.right(90)
        grid_turtle.end_fill()

    # Draw hidden cell
    else:
        grid_turtle.color("lightgrey")
        grid_turtle.begin_fill()
        for _ in range(4):
            grid_turtle.forward(CELL_SIZE)
            grid_turtle.right(90)
        grid_turtle.end_fill()


def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            draw_cell(row, col)


def reveal(row, col):
    global game_over

    if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
        return
    if revealed[row][col] or flags[row][col]:
        return

    revealed[row][col] = True
    draw_cell(row, col)

    if mines[row][col]:
        game_over = True
        reveal_all_mines()
        print("Game Over")
        return

    if count_adjacent_mines(row, col) == 0:
        for r in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
            for c in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
                reveal(r, c)

def reveal_all_mines():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if mines[r][c]:
                revealed[r][c] = True
    draw_grid()


def check_win():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if not mines[r][c] and not revealed[r][c]:
                return False
    return True


def handle_click(x, y):
    global first_click

    if game_over:
        return

    col = int((x + (GRID_SIZE * CELL_SIZE) // 2) // CELL_SIZE)
    row = int(((GRID_SIZE * CELL_SIZE) // 2 - y) // CELL_SIZE)

    if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
        return

    if first_click:
        place_mines(row, col)
        first_click = False

    if not flags[row][col]:
        reveal(row, col)

    if check_win():
        print("You Win!")

def handle_right_click(x, y):
    if game_over or first_click:
        return

    col = int((x + (GRID_SIZE * CELL_SIZE) // 2) // CELL_SIZE)
    row = int(((GRID_SIZE * CELL_SIZE) // 2 - y) // CELL_SIZE)

    if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
        return

    flags[row][col] = not flags[row][col]
    draw_cell(row, col)


# Bind mouse events
screen.onclick(handle_click)
screen.onscreenclick(handle_right_click, btn=3)

draw_grid()
turtle.done()
