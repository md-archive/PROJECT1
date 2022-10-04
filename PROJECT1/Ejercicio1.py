import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
def square(x):
        for _ in range(4):
                t.fd(x)
                t.rt(90)
for _ in range(10):
        square(100)
        t.rt(360/10)