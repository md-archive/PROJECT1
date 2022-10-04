import turtle
t = turtle.Turtle()
def star(l, n):
        for _ in range(n):
                t.fd(l)
                t.bk(l)
                t.rt(360/n)
star(100, 20)