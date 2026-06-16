import turtle
import time
import random

# -----------------------------
# Global game variables
# -----------------------------
size = 40
start_time = 0
won = False
mode = None
in_play = False

grid = [[0] * 9 for _ in range(9)]
locked = [[0] * 9 for _ in range(9)]
selected_cell = None
lives = 3
flash_cell = None

hover_cell = None
mouse_x = 0
mouse_y = 0

# -----------------------------
# Setup UI Turtles
# -----------------------------
t_draw = turtle.Turtle()
t_text = turtle.Turtle()
t_time = turtle.Turtle()

for t in (t_draw, t_text, t_time):
    t.speed(0)
    t.hideturtle()
    t.penup()

screen = turtle.Screen()
screen.setup(500, 650)
screen.tracer(0)
screen.title("Neon Sudoku")
screen.bgcolor("#050816")

# -----------------------------
# Core Sudoku logic
# -----------------------------
def is_allowed(r, c, val):
    if val == 0:
        return True

    for i in range(9):
        if (grid[r][i] == val and i != c) or (grid[i][c] == val and i != r):
            return False

    box_r0 = (r // 3) * 3
    box_c0 = (c // 3) * 3
    for dr in range(3):
        for dc in range(3):
            rr = box_r0 + dr
            cc = box_c0 + dc
            if (rr != r or cc != c) and grid[rr][cc] == val:
                return False

    return True


def solve_board():
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for val in range(1, 10):
                    if is_allowed(r, c, val):
                        grid[r][c] = val
                        if solve_board():
                            return True
                        grid[r][c] = 0
                return False
    return True


def check_win():
    global won
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0 or not is_allowed(r, c, grid[r][c]):
                return False
    won = True
    return True


def reset_board(full_reset_mode=True):
    global grid, locked, selected_cell, lives, flash_cell, won, in_play, mode

    grid = [[0] * 9 for _ in range(9)]
    locked = [[0] * 9 for _ in range(9)]
    selected_cell = None
    lives = 3
    flash_cell = None
    won = False
    in_play = False

    if full_reset_mode:
        mode = None


def clear_flash():
    global flash_cell
    flash_cell = None
    draw_everything()

# -----------------------------
# Drawing helpers
# -----------------------------
def draw_glow_rect(x, y, w, h, color, width=2):
    t_draw.goto(x, y)
    t_draw.pendown()
    t_draw.pensize(width)
    t_draw.pencolor(color)
    for _ in range(2):
        t_draw.forward(w)
        t_draw.left(90)
        t_draw.forward(h)
        t_draw.left(90)
    t_draw.penup()


def draw_filled_rect(x, y, w, h, color):
    t_draw.goto(x, y)
    t_draw.fillcolor(color)
    t_draw.begin_fill()
    for _ in range(2):
        t_draw.forward(w)
        t_draw.left(90)
        t_draw.forward(h)
        t_draw.left(90)
    t_draw.end_fill()

# -----------------------------
# Drawing: Menu
# -----------------------------
def draw_menu():
    t_draw.clear()
    t_text.clear()
    t_time.clear()

    t_text.goto(0, 180)
    t_text.color("#00E5FF")
    t_text.write("NEON SUDOKU", align="center", font=("Arial", 24, "bold"))

    t_text.goto(0, 150)
    t_text.color("#FFEA00")
    t_text.write("Select Difficulty", align="center", font=("Arial", 14))

    labels = ["EASY", "MEDIUM", "HARD", "CUSTOM"]
    colors = ["#00C853", "#FFD600", "#D50000", "#651FFF"]

    for i, name in enumerate(labels):
        y_top = 80 - i * 60
        x_left = -100
        w, h = 200, 40

        draw_glow_rect(x_left, y_top, w, h, colors[i], width=3)
        draw_filled_rect(x_left, y_top, w, h, "#1A1A2E")

        t_text.goto(0, y_top + 10)
        t_text.color(colors[i])
        t_text.write(name, align="center", font=("Arial", 14, "bold"))

# -----------------------------
# Drawing: Board
# -----------------------------
def draw_board():
    t_draw.clear()
    t_text.clear()

    draw_filled_rect(-190, -190, 380, 380, "#0A0F1F")

    if hover_cell and not selected_cell and in_play and lives > 0 and not won:
        r, c = hover_cell
        draw_filled_rect(-180 + c * size, -180 + r * size, size, size, "#1E293B")

    if selected_cell and not won and lives > 0 and in_play:
        r, c = selected_cell
        draw_filled_rect(-180 + c * size, -180 + r * size, size, size, "#FFF176")

    if flash_cell:
        fr, fc = flash_cell
        draw_filled_rect(-180 + fc * size, -180 + fr * size, size, size, "#FF5252")

    for i in range(10):
        t_draw.pensize(3 if i % 3 == 0 else 1)
        t_draw.pencolor("#00E5FF" if i % 3 == 0 else "#37474F")

        t_draw.goto(-180 + i * size, -180)
        t_draw.pendown()
        t_draw.goto(-180 + i * size, 180)
        t_draw.penup()

        t_draw.goto(-180, -180 + i * size)
        t_draw.pendown()
        t_draw.goto(180, -180 + i * size)
        t_draw.penup()

    for i in range(1, 10):
        x0 = -180 + (i - 1) * size
        y0 = -220

        draw_glow_rect(x0, y0, size, size, "#00E5FF", width=2)
        draw_filled_rect(x0, y0, size, size, "#0A1929")

        t_text.goto(x0 + 20, y0 - 35)
        t_text.color("#E0F7FA")
        t_text.write(str(i), align="center", font=("Arial", 14, "bold"))

    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                t_text.goto(-180 + c * size + 20, -180 + r * size + 8)
                if locked[r][c]:
                    t_text.color("#40C4FF")
                    style = "bold"
                else:
                    t_text.color("#FFAB40")
                    style = "normal"
                t_text.write(str(grid[r][c]), align="center",
                             font=("Arial", 16, style))

    # FIXED SOLVE BUTTON CLICK AREA
    draw_glow_rect(-60, -270, 120, 40, "#FF1744", width=3)
    draw_filled_rect(-60, -270, 120, 40, "#1A1A2E")
    t_text.goto(0, -280)
    t_text.color("#FF5252")
    t_text.write("SOLVE", align="center", font=("Arial", 14, "bold"))

    draw_glow_rect(-50, 210, 100, 30, "#7C4DFF", width=2)
    draw_filled_rect(-50, 210, 100, 30, "#1A1A2E")
    t_text.goto(0, 200)
    t_text.color("#B388FF")
    t_text.write("MENU", align="center", font=("Arial", 12, "bold"))

    if won:
        t_text.goto(0, 195)
        t_text.color("#00E676")
        t_text.write("COMPLETED! 🎉", align="center", font=("Arial", 16, "bold"))
    elif lives <= 0:
        t_text.goto(0, 195)
        t_text.color("#FF3D00")
        t_text.write("GAME OVER! ❌", align="center", font=("Arial", 16, "bold"))

def draw_everything():
    if mode is None:
        draw_menu()
    else:
        draw_board()
    screen.update()

# -----------------------------
# Game setup helpers
# -----------------------------
def generate_puzzle(difficulty):
    global grid, locked

    grid = [[0] * 9 for _ in range(9)]
    locked = [[0] * 9 for _ in range(9)]

    solve_board()

    keep = {"easy": 45, "medium": 32, "hard": 22}[difficulty]
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    to_remove = 81 - keep
    for r, c in cells[:to_remove]:
        grid[r][c] = 0

    for r in range(9):
        for c in range(9):
            locked[r][c] = 1 if grid[r][c] != 0 else 0

def start_game(selected_mode):
    global mode, in_play, start_time, won, lives, selected_cell, flash_cell

    reset_board(full_reset_mode=False)
    mode = selected_mode
    in_play = True
    won = False
    lives = 3
    selected_cell = None
    flash_cell = None
    start_time = time.time()

    if mode in ("easy", "medium", "hard"):
        generate_puzzle(mode)

    draw_everything()

# -----------------------------
# Input handling
# -----------------------------
def handle_click(x, y):
    global mode, selected_cell, won, lives, flash_cell, in_play

    if mode is not None and -50 < x < 50 and 180 < y < 240:
        reset_board(full_reset_mode=True)
        draw_everything()
        return

    if mode is None and -100 < x < 100:
        labels = ["easy", "medium", "hard", "custom"]
        for i, diff in enumerate(labels):
            y_top = 80 - i * 60
            if y_top - 40 < y < y_top:
                start_game(diff)
                return

    if mode is None:
        return

    if lives <= 0 or won:
        return

    if -180 < x < 180 and -180 < y < 180:
        c = int((x + 180) // size)
        r = int((y + 180) // size)
        if not locked[r][c]:
            selected_cell = (r, c)
        draw_everything()
        return

    if selected_cell and -180 < x < 180 and -260 < y < -220:
        val = int((x + 180) // size) + 1
        r, c = selected_cell

        if is_allowed(r, c, val):
            grid[r][c] = val
            if mode == "custom":
                locked[r][c] = 1
            check_win()
        else:
            lives -= 1
            flash_cell = (r, c)
            screen.ontimer(clear_flash, 500)

        selected_cell = None
        draw_everything()
        return

    # FIXED SOLVE BUTTON CLICK AREA
    if -60 < x < 60 and -270 < y < -230:
        solve_board()
        won = True
        in_play = False
        draw_everything()
        return

# -----------------------------
# Hover tracking (FIXED)
# -----------------------------
def track_mouse(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y

def update_hover():
    global hover_cell

    x, y = mouse_x, mouse_y

    if mode is not None and -180 < x < 180 and -180 < y < 180:
        c = int((x + 180) // size)
        r = int((y + 180) // size)
        hover_cell = (r, c)
    else:
        hover_cell = None

    draw_everything()
    screen.ontimer(update_hover, 10)

# -----------------------------
# Timer and lives display
# -----------------------------
def run_timer_and_lives():
    t_time.clear()

    if mode is not None and in_play and not won and lives > 0:
        t_time.goto(-190, 195)
        t_time.color("#FF5252")
        t_time.write(f"Lives: {'❤ ' * lives}", align="left",
                     font=("Arial", 12, "bold"))

        t_time.goto(100, 195)
        t_time.color("#00E5FF")
        elapsed = int(time.time() - start_time)
        t_time.write(f"Time: {elapsed // 60:02d}:{elapsed % 60:02d}",
                     font=("Arial", 12, "bold"))

    screen.ontimer(run_timer_and_lives, 1000)

# -----------------------------
# Main
# -----------------------------
screen.onscreenclick(handle_click)

# FIXED: smooth hover tracking using Tk canvas Motion event
canvas = screen.getcanvas()

def _tk_motion(event):
    # Convert Tk canvas coords (origin top-left) to turtle coords (origin center)
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    tx = event.x - w / 2
    ty = h / 2 - event.y
    track_mouse(tx, ty)

canvas.bind('<Motion>', _tk_motion)

draw_everything()
update_hover()
run_timer_and_lives()

turtle.done()

