import tkinter as tk
from random import randrange, choice

window = tk.Tk()
window.title("Smooth Fly Swatter Game")
c = tk.Canvas(window, width=600, height=500, bg='#87CEEB') 
c.pack()

score = 0
time_left = 30
game_over = False

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

class Bug():
    def __init__(self, x, y, bug_image):
        self.x = x
        self.y = y
        self.dx = choice([-4, -3, 3, 4])
        self.dy = choice([-4, -3, 3, 4])
        
        self.obj = c.create_image(x, y, image=bug_image)
            
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        self.move()

    def move(self):
        if game_over:
            return

        coords = c.coords(self.obj)
        if not coords: 
            return
            
        current_x, current_y = coords[0], coords[1]
        
        if current_x <= 0 or current_x >= 600:
            self.dx *= -1 
        if current_y <= 0 or current_y >= 500:
            self.dy *= -1 
            
        c.move(self.obj, self.dx, self.dy)
        window.after(30, self.move)

    def destroy(self, event): 
        if not game_over:
            c.delete(self.obj)
            update_score()
            print('Got one!')

class Fly(Bug):
    img = tk.PhotoImage(file='small_fly.png')
    def __init__(self, x, y):
        super().__init__(x, y, Fly.img)

class LadyBug(Bug):
    img = tk.PhotoImage(file='small_ladybug.png')
    def __init__(self, x, y):
        super().__init__(x, y, LadyBug.img)


class Bananas(Fruit)
    img = tk.Photoimage(file='banabana.png')
    def_init_(self, x, y)


for i in range(10):
    Fly(randrange(50, 550), randrange(50, 450))
    LadyBug(randrange(50, 550), randrange(50, 450))


countdown()
window.mainloop()











