#give them option easy(fills in a lot of sqaures), medium(fills in a decent amount of squares), hard(fills in very few squares)and custom where they can fill in the squares themselves and then solve it. also add a timer to see how long it takes them to solve.
#remove when done.
#custom is this one right now.
import turtle

# Basic settings
CELL_SIZE = 40
GRID_SIZE = 9
PANEL_Y_OFFSET = -80  # Y-offset for numbers below the grid
SELECTED_CELL = None

# Set up screen
screen = turtle.Screen()
screen.setup(width=500, height=600)
screen.title("SUPERMEGAULTRACOOLSKIBIDITUFFSIGMASOCRATESTHE67AURAFARMER's Sudoku")

# Turtle for drawing
draw_t = turtle.Turtle()
draw_t.speed(0)
draw_t.hideturtle()

# Turtle for text (numbers)
text_t = turtle.Turtle()
text_t.speed(0)
text_t.hideturtle()
text_t.penup()

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_line(t, x1, y1, x2, y2, width=1):
    t.width(width)
    jump_to(t, x1, y1)
    t.goto(x2, y2)

def draw_sudoku_grid():
    total_size = CELL_SIZE * GRID_SIZE
    half = total_size / 2
    
    # Draw vertical lines
    for i in range(GRID_SIZE + 1):
        x = -half + i * CELL_SIZE
        w = 3 if i % 3 == 0 else 1
        draw_line(draw_t, x, -half, x, half, width=w)
        
    # Draw horizontal lines
    for i in range(GRID_SIZE + 1):
        y = -half + i * CELL_SIZE
        w = 3 if i % 3 == 0 else 1
        draw_line(draw_t, -half, y, half, y, width=w)

def draw_number_panel():
    total_size = CELL_SIZE * GRID_SIZE
    half = total_size / 2
    y_pos = -half + PANEL_Y_OFFSET
    
    # Draw panel boxes
    for i in range(1, 10):
        x_pos = -half + (i - 1) * CELL_SIZE
        jump_to(draw_t, x_pos - CELL_SIZE/2, y_pos - CELL_SIZE/2)
        
        # Draw box outline
        for _ in range(4):
            draw_t.forward(CELL_SIZE)
            draw_t.right(90)
            
        # Write the number (1-9)
        text_t.goto(x_pos, y_pos)
        text_t.write(str(i), align="center", font=("Arial", 16, "normal"))

def handle_click(x, y):
    global SELECTED_CELL
    total_size = CELL_SIZE * GRID_SIZE
    half = total_size / 2
    
    # Check Grid Clicks
    if -half < x < half and -half < y < half:
        col = int((x + half) // CELL_SIZE)
        row = int((y + half) // CELL_SIZE)
        SELECTED_CELL = (row, col)
        print(f"Selected Cell: Row {row}, Col {col}")
        
    # Check Number Panel Clicks
    panel_y = -half + PANEL_Y_OFFSET
    if panel_y - CELL_SIZE/2 < y < panel_y + CELL_SIZE/2:
        if -half < x < half:
            number = int((x + half) // CELL_SIZE) + 1
            if SELECTED_CELL:
                row, col = SELECTED_CELL
                # Calculate screen coordinates for the selected cell
                center_x = -half + col * CELL_SIZE + CELL_SIZE / 2
                center_y = -half + row * CELL_SIZE + CELL_SIZE / 2
                
                # Place number on grid
                text_t.goto(center_x, center_y - 15)
                text_t.write(str(number), align="center", font=("Arial", 16, "bold"))
                print(f"Placed {number} at {SELECTED_CELL}")

# Initialize the game board
draw_sudoku_grid()
draw_number_panel()

# Listen for mouse clicks
screen.onscreenclick(handle_click)
screen.listen()

turtle.done()
