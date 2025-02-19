import tkinter as tk
import random

# 1Initialize the main window
window = tk.Tk()
window.title("Tank War")
window.geometry('800x600')
window.resizable(False, False)

# Create a canvas for drawing
canvas = tk.Canvas(window, bg='white', width=800, height=600)
canvas.pack()

# Create tank class
class Tank:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.tank = canvas.create_rectangle(x, y, x+50, y+30, fill="green")
        self.cannon = canvas.create_rectangle(x+20, y-10, x+30, y, fill="black")
        self.x = x
        self.y = y
        self.speed = 10
        self.bullets = []

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
            self.canvas.move(self.tank, -self.speed, 0)
            self.canvas.move(self.cannon, -self.speed, 0)

    def move_right(self):
        if self.x < 750:
            self.x += self.speed
            self.canvas.move(self.tank, self.speed, 0)
            self.canvas.move(self.cannon, self.speed, 0)

    def move_up(self):
        if self.y > 30:
            self.y -= self.speed
            self.canvas.move(self.tank, 0, -self.speed)
            self.canvas.move(self.cannon, 0, -self.speed)

    def move_down(self):
        if self.y < 570:
            self.y += self.speed
            self.canvas.move(self.tank, 0, self.speed)
            self.canvas.move(self.cannon, 0, self.speed)

    def fire(self):
        bullet = self.canvas.create_rectangle(self.x+23, self.y-10, self.x+27, self.y-20, fill="red")
        self.bullets.append(bullet)
        self.move_bullets()

    def move_bullets(self):
        for bullet in self.bullets:
            self.canvas.move(bullet, 0, -10)
            bullet_coords = self.canvas.coords(bullet)
            if bullet_coords and bullet_coords[1] <= 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
            elif target.hit_check(bullet_coords):
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
                target.reset_position()
        window.after(50, self.move_bullets)

# Create target class
class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.target = canvas.create_oval(700, 50, 750, 100, fill="blue")
        self.speed = 5
        self.move_target()

    def move_target(self):
        self.canvas.move(self.target, -self.speed, 0)
        coords = self.canvas.coords(self.target)
        if coords[0] <= 0 or coords[2] >= 800:
            self.speed = -self.speed
        window.after(100, self.move_target)

    def hit_check(self, bullet_coords):
        if not bullet_coords:
            return False
        target_coords = self.canvas.coords(self.target)
        if (bullet_coords[0] >= target_coords[0] and bullet_coords[2] <= target_coords[2] and
            bullet_coords[1] <= target_coords[3] and bullet_coords[3] >= target_coords[1]):
            return True
        return False

    def reset_position(self):
        self.canvas.coords(self.target, random.randint(100, 700), 50, random.randint(150, 750), 100)

# Initialize objects
tank = Tank(canvas, 375, 500)
target = Target(canvas)

# Key bindings
def key_pressed(event):
    if event.keysym == "Left":
        tank.move_left()
    elif event.keysym == "Right":
        tank.move_right()
    elif event.keysym == "Up":
        tank.move_up()
    elif event.keysym == "Down":
        tank.move_down()
    elif event.keysym == "space":
        tank.fire()

window.bind("<KeyPress>", key_pressed)

window.mainloop()
