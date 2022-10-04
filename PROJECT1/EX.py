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
def func_draw_square(x):
        for _ in range(4):
            t.fd(x)
            t.rt(90)
for _ in range(10):
        func_draw_square(100)
        t.rt(360/10)

    # ADDITIONAL OPTIONS
def func_draw_square_fille():
    print('Has elegido el Ejercicio 1 Filled Square')
def func_draw_multi_square():
    print('Has elegido el Ejercicio 1 MultiSquare')
    
# DRAW STAR WITH FOR LOOP
def func_draw_star(l, n):
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360/n)
func_draw_star(100, 20)

# DRAW RANDOM STARS WITH FOR LOOP
def rand_draw_star(x, y, l, n):
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
        rand_draw_star(random.randint(-300, 300),
             random.randint(-300, 300),
             random.randint(10, 150),
        random.randint(3, 30))


# DRAW POLYGON 
def polygon(l, n):
    for i in range(7):
        t.forward(l)
        t.right(n)

polygon(100, 51.6)

def func_draw_circle():
    print('Has elegido el Ejercicio 1 Circle')
    
def func_draw_filled_circle():
    print('Has elegido el Ejercicio 1 Filled Circle')
    
def func_draw_square_circle():
    print('Has elegido el Ejercicio 1 Square Circles')