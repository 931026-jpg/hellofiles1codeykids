import turtle, time, random

# Global game variables
size, start_time, won, mode = 40, 0, False, None
grid = [[0] * 9 for _ in range(9)]
locked = [[0] * 9 for _ in range(9)]
selected_cell = None  
lives = 3             # Player starts with 3 lives
flash_cell = None     # Tracks which cell should flash red

# Setup UI Turtles
t_draw, t_text, t_time = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
for t in (t_draw, t_text, t_time): 
    t.speed(0); t.hideturtle(); t.penup()

screen = turtle.Screen()
screen.setup(500, 650)
screen.tracer(0)

def is_allowed(r, c, val):
    """Checks if a number fits safely in the row, column, and 3x3 box."""
    for i in range(9):
        if (grid[r][i] == val and i != c) or (grid[i][c] == val and i != r): 
            return False
        box_r, box_c = (r // 3) * 3 + i // 3, (c // 3) * 3 + i % 3
        if grid[box_r][box_c] == val and (box_r != r or box_c != c): 
            return False
    return True

def solve_board():
    """Fills the grid using standard Sudoku backtracking rules."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for val in random.sample(range(1, 10), 9):
                    if is_allowed(r, c, val):
                        grid[r][c] = val
                        if solve_board(): return True
                        grid[r][c] = 0
                return False
    return True

def check_win():
    """Checks if the board is completely full and correct."""
    global won
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0 or not is_allowed(r, c, grid[r][c]):
                return False
    won = True
    return True

def clear_flash():
    """Clears the red mistake flash and redraws the board."""
    global flash_cell
    flash_cell = None
    draw_everything()

def draw_everything():
    """Draws the main menu or the active gameplay graphics."""
    t_draw.clear(); t_text.clear()
    
    if mode is None:
        t_text.goto(0, 150); t_text.write("SUDOKU", align="center", font=("Arial", 20, "bold"))
        for i, name in enumerate(["EASY", "MEDIUM", "HARD", "CUSTOM"]):
            t_draw.goto(-80, 70 - i * 50); t_draw.begin_fill()
            t_draw.fillcolor("#4CAF50" if i < 3 else "#008CBA")
            for _ in range(2): t_draw.forward(160); t_draw.right(90); t_draw.forward(35); t_draw.right(90)
            t_draw.end_fill()
            t_text.goto(0, 48 - i * 50); t_text.color("white")
            t_text.write(name, align="center", font=("Arial", 12, "bold"))
    else:
        # Highlight selected cell if active
        if selected_cell and not won and lives > 0:
            r, c = selected_cell
            t_draw.goto(-180 + c * size, -180 + r * size)
            t_draw.begin_fill(); t_draw.fillcolor("#FFF59D")  # Soft yellow highlight
            for _ in range(4): t_draw.forward(size); t_draw.left(90)
            t_draw.end_fill()

        # Flash cell red if a mistake was made
        if flash_cell:
            fr, fc = flash_cell
            t_draw.goto(-180 + fc * size, -180 + fr * size)
            t_draw.begin_fill(); t_draw.fillcolor("#EF5350")  # Smooth red color
            for _ in range(4): t_draw.forward(size); t_draw.left(90)
            t_draw.end_fill()

        # Draw the 9x9 grid lines
        for i in range(10):
            t_draw.width(3 if i % 3 == 0 else 1)
            t_draw.goto(-180 + i * size, -180); t_draw.pendown(); t_draw.goto(-180 + i * size, 180); t_draw.penup()
            t_draw.goto(-180, -180 + i * size); t_draw.pendown(); t_draw.goto(180, -180 + i * size); t_draw.penup()
            
        # Draw bottom input panel numbers (1-9)
        for i in range(1, 10):
            t_draw.goto(-180 + (i - 1) * size, -220); t_draw.pendown()
            for _ in range(4): t_draw.forward(size); t_draw.right(90)
            t_draw.penup()
            t_text.goto(-180 + (i - 1) * size + 20, -255); t_text.color("black")
            t_text.write(str(i), align="center", font=("Arial", 14))
            
        # Write numbers onto the board
        for r in range(9):
            for c in range(9):
                if grid[r][c] != 0:
                    t_text.goto(-180 + c * size + 20, -180 + r * size + 8)
                    t_text.color("#1A237E" if locked[r][c] else "black")
                    t_text.write(str(grid[r][c]), align="center", font=("Arial", 14, "bold" if locked[r][c] else "normal"))
                    
        # Draw special Solve Button for Custom mode
        if mode == "custom":
            t_draw.goto(-50, -270); t_draw.begin_fill(); t_draw.fillcolor("#E74C3C")
            for _ in range(2): t_draw.forward(100); t_draw.right(90); t_draw.forward(35); t_draw.right(90)
            t_draw.end_fill()
            t_text.goto(0, -292); t_text.color("white"); t_text.write("SOLVE", align="center", font=("Arial", 12, "bold"))
            
        # Visual status messages top center
        if won: 
            t_text.goto(0, 195); t_text.color("green"); t_text.write("COMPLETED! 🎉", align="center", font=("Arial", 16, "bold"))
        elif lives <= 0:
            t_text.goto(0, 195); t_text.color("red"); t_text.write("GAME OVER! ❌", align="center", font=("Arial", 16, "bold"))
            
    screen.update()

def handle_click(x, y):
    """Main click router managing menu button presses and placement targets."""
    global mode, start_time, selected_cell, won, lives, flash_cell
    
    # If game is over or won, stop handling actions
    if lives <= 0 or won: return

    # 1. Menu Interactions
    if mode is None and -80 < x < 80:
        for i, diff in enumerate(["easy", "medium", "hard", "custom"]):
            if 35 - i * 50 < y < 70 - i * 50: 
                mode = diff
        if mode and mode != "custom":
            solve_board()
            removals = 81 - {"easy": 45, "medium": 32, "hard": 22}[mode]
            for r, c in random.sample([(r, c) for r in range(9) for c in range(9)], removals): 
                grid[r][c] = 0
            for r in range(9):
                for c in range(9): 
                    locked[r][c] = 1 if grid[r][c] else 0
            mode, start_time = "play", time.time()
        elif mode == "custom": 
            start_time = time.time()
        draw_everything()
        return

    # 2. Clicking a Grid Square to Select It
    if mode and -180 < x < 180 and -180 < y < 180:
        c, r = int((x + 180) // size), int((y + 180) // size)
        if not locked[r][c]:  
            selected_cell = (r, c)
        draw_everything()
        return

    # 3. Clicking the Bottom Number Strip (1-9) to Apply Selected Box Value
    if mode and selected_cell and -180 < x < 180 and -260 < y < -220:
        val = int((x + 180) // size) + 1
        r, c = selected_cell
        
        if is_allowed(r, c, val):
            grid[r][c] = val
            if mode == "custom": 
                locked[r][c] = 1 
            check_win()
        else:
            # Code handles mistake pathing dynamically
            if mode != "custom":
                lives -= 1
                flash_cell = (r, c)
                screen.ontimer(clear_flash, 500)  # Keeps cell red for exactly half a second
        
        selected_cell = None  
        draw_everything()
        return

    # 4. Custom Solve Button Click
    if mode == "custom" and -50 < x < 50 and -305 < y < -270:
        mode = "play"
        solve_board()
        won = True
        draw_everything()

def run_timer_and_lives():
    """Updates game duration display and remaining player lives status."""
    if mode == "play" and not won and lives > 0:
        t_time.clear()
        
        # Display Lives Left on Top Left
        t_time.goto(-180, 195); t_time.color("red")
        t_time.write(f"Lives: {'❤️ ' * lives}", align="left", font=("Arial", 12, "bold"))
        
        # Display Running Timer on Top Right
        t_time.goto(100, 195); t_time.color("black")
        elapsed = int(time.time() - start_time)
        t_time.write(f"Time: {elapsed // 60:02d}:{elapsed % 60:02d}", font=("Arial", 12, "bold"))
        
    screen.ontimer(run_timer_and_lives, 1000)

screen.onscreenclick(handle_click)
draw_everything()
run_timer_and_lives()
turtle.done()
