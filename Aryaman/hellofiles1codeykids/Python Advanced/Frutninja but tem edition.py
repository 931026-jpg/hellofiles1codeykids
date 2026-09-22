import tkinter as tk
from random import randrange, choice

window = tk.Tk()
window.title("Fruit Ninja - Ultimate Edition")
c = tk.Canvas(window, width=600, height=500, bg='#87CEEB') 
c.pack()

score = 0
time_left = 30
game_over = False

active_fruits = []
IMAGES = {}

def load_and_scale(filename):
    """Loads an image and scales it down if it's too massive for the screen."""
    img = tk.PhotoImage(file=filename)
    
    if img.width() > 100:
        scale_factor = img.width() // 60  
        if scale_factor > 1:
            img = img.subsample(scale_factor, scale_factor)
    return img

def load_images():
    try:
        IMAGES['watermelon'] = load_and_scale('melonmelon.png')
        IMAGES['bananas'] = load_and_scale('banabana.png')
        IMAGES['bomb'] = load_and_scale('bombboombombboom.png') 
        IMAGES['coconut'] = load_and_scale('coconutnunit.png')
        print("Success: Images loaded AND scaled perfectly!")
    except tk.TclError as e:
        print("\n--- IMAGE ERROR ---")
        print(f"File missing or corrupted: {e}")
        print("-------------------\n")

def update_score():
    global score
    score += 1

def countdown():
    global time_left, game_over
    if time_left > 0:
        time_left -= 1
        window.after(1000, countdown) 
    else:
        game_over = True
        print(f"Time's up! Final score: {score}")

class Fruit():
    def __init__(self, x, y, image_key): 
        self.x = x
        self.y = y
        self.dx = choice([-4, -3, 3, 4])
        self.dy = choice([-4, -3, 3, 4])
        
        self.obj = c.create_image(x, y, image=IMAGES[image_key]) 
            
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)

    def move(self):
        coords = c.coords(self.obj)
        if not coords: 
            return
            
        current_x, current_y = coords[0], coords[1]
        
        if current_x <= 0 or current_x >= 600:
            self.dx *= -1 
        if current_y <= 0 or current_y >= 500:
            self.dy *= -1 
            
        c.move(self.obj, self.dx, self.dy)

    def destroy(self, event): 
        if not game_over:
            c.delete(self.obj)
            if self in active_fruits:
                active_fruits.remove(self)
            update_score()
            print(f'Got one! Score: {score}')

class Watermelon(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 'watermelon')

class Bananas(Fruit):
    def __init__(self, x, y): 
        super().__init__(x, y, 'bananas')

class Bomb(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 'bomb')
        
    def destroy(self, event):
        global game_over
        if not game_over:
            game_over = True
            print("Hit a bomb! Game Over!")

class Coconut(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y, 'coconut')

def game_loop():
    if not game_over:
        for fruit in active_fruits[:]:
            fruit.move()
        window.after(30, game_loop)


load_images()

if len(IMAGES) == 4:
    for i in range(10):
        active_fruits.append(Bomb(randrange(50, 550), randrange(50, 450)))
        active_fruits.append(Coconut(randrange(50, 550), randrange(50, 450)))
        active_fruits.append(Watermelon(randrange(50, 550), randrange(50, 450)))
        active_fruits.append(Bananas(randrange(50, 550), randrange(50, 450)))

game_loop()
countdown()

window.mainloop()