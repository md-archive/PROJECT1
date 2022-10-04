import turtle
import random
t = turtle.Turtle()
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