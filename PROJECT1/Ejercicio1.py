import turtle
import random

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
# DRAW SQUARE WITH FOR LOOP
def draw_square(x):
        for _ in range(4):
            t.fd(x)
            t.rt(90)
for _ in range(10):
        draw_square(100)
        t.rt(360/10)

# DRAW STAR WITH FOR LOOP
def star(l, n):
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360/n)
star(100, 20)

# DRAW POLYGON 
def polygon(l, n):
    for i in range(7):
        t.forward(l)
        t.right(n)

polygon(100, 51.6)

# DRAW RANDOM STARS WITH FOR LOOP
def star(x, y, l, n):
        t.penup()
        t.home()
        t.fd(x)
        t.lt(90)
        t.fd(y)
        t.pendown()
        for _ in range(n):
            t.fd(l)
            t.bk(l)
            t.rt(360/n)
for _ in range(20):
        t.speed(500)
        star(random.randint(-300, 300),
             random.randint(-300, 300),
             random.randint(10, 150),
        random.randint(3, 30))
