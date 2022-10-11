import turtle
import random
import math
import time
import sys
# INITIALISING VARIABLES

# DECLARING (MODIFIABLE) CONSTANTS
FW_1 = 50
FW_2 = 20
FW_3 = 150
# SQUARE CONSTANTS
SIDES = 4
DEGREES = 90
DISTANCE = 100
FLOWER = 10
# GENERAL ROTATION SETTING CONSTANT
ROTATION_DEGREES = 360
CIRCLED_SQUARES = 720
# DRAW SQUARED CIRCLES CONSTANTS
QTY_SQUARES= 200
OBJECT_POSITION = 300 
# GENERAL OBJECT SIZE CONSTANT
SIZE = 100
# NUMBER OF LINES TO DRAW
LINES = 40
# POLYGON SIDES AND SIZE TO DRAW
POLYGON_SIDES = 8
POLYGON_SIZE = 100
# RADIANT 
RAD_EQ_TOTAL_SIZE = 50
STAR_QTY = 20

QTY = 20

COLOUR = "#5050FF"
# FUNCTIONS LIST


def funcion1square():
    t = turtle.Turtle()

    for _ in range(SIDES):
        t.right(DEGREES)
        t.forward(DISTANCE)
    time.sleep(5)
    t.home()
    t.clear()
def funcion1filledSquare():
    t = turtle.Turtle()
    t.fillcolor(COLOUR)
    t.begin_fill()
    for _ in range(SIDES):
        t.right(DEGREES)
        t.forward(DISTANCE)

    t.end_fill()
    time.sleep(10)
    t.home()
    t.clear()
def funcion1multiSquare():
    t= turtle.Turtle()
    def poly():
        for _ in range(POLYGON_SIDES):
            t.forward(POLYGON_SIZE)
            t.right(ROTATION_DEGREES / POLYGON_SIDES)
    for _ in range(FW_2):
        poly()
        t.rt(360.0 / FW_2)
        t.speed(9)
# def funcion1multiSquare(): 
#     def many_squares(SIDES):
#         t = turtle.Turtle()
#         t.speed(8)
#         for _ in range(SIDES):
#             funcion1square()
#             t.right(360.0 / SIDES)
#     def poly(SIDES,DISTANCE):
#         t = turtle.Turtle()
#         for _ in range(SIDES):
#             t.forward(DISTANCE)
#             t.right(360.0 / SIDES)
#     def many_poly(SIDES, number, DISTANCE):
#         t = turtle.Turtle()
#         for _ in range(number):
#             poly(SIDES, DISTANCE)
#             t.right(360.0 / number)
#     many_squares(SIDES)
#     many_poly(7,16,100)

def funcion1polygon():
    t = turtle.Turtle()
    for _ in range(POLYGON_SIDES):
        t.forward(POLYGON_SIZE)
        t.right(ROTATION_DEGREES / POLYGON_SIDES)
    time.sleep(5)
    t.home()
    t.clear()
def funcion1circle():
    t = turtle.Turtle()
    total = 0
    t.setposition(0, 0)
    total = 2 * math.pi * RAD_EQ_TOTAL_SIZE
    num = int(total)
    for _ in range(num):
        t.forward(1.5)
        t.left(1.15)
    t.home()
    t.clear()
def funcion1filledCircle():
    t = turtle.Turtle()
    t.fillcolor(COLOUR)
    t.begin_fill()
    total = 0
    t.setposition(0, 0)
    total = 2 * math.pi * RAD_EQ_TOTAL_SIZE
    num = int(total)
    for _ in range(num):
        t.forward(1.5)
        t.left(1.15)
    t.end_fill()
    time.sleep(5)
    t.home()
    t.clear()

def funcion1squareCircles():
    t = turtle.Turtle()
    def square(data):
        for _ in range(SIDES):
            t.right(DEGREES)
            t.forward(data)
    
    for _ in range(CIRCLED_SQUARES):
        square(QTY_SQUARES)
        t.rt(ROTATION_DEGREES / OBJECT_POSITION)
def funcion1star():
    t = turtle.Turtle()
    for _ in range(LINES):
        t.forward(SIZE)
        t.back(SIZE)
        t.right(ROTATION_DEGREES/LINES)
    t.home()
    t.clear()
def funcion1stars():
    t = turtle.Turtle()

    t.penup()
    t.home()
    t.forward(FW_1)
    t.left(DEGREES)
    t.forward(FW_2)
    t.pendown()
    for _ in range(LINES):
        t.forward(FW_3)
        t.back(FW_3)
        t.right(DEGREES/LINES)
    # randint = Random star position
    # number shows where the turtle will be displayed
    #
    for _ in range(STAR_QTY):
        funcion1stars(random.randint(-300, 300),
                      random.randint(-300, 300),
                      random.randint(10, 150),
                      random.randint(3, 30))
def funcion1gridcircles():
    
    t = turtle.Turtle()
    def grid(sx, sy, nx, ny):
        for x in range(nx):
            for y in range(ny):
                t.penup()
                t.goto(sx + x * 50, sy + y * 50)
                t.pendown()
                t.circle(25)
    grid(-100,-100,5,4)
def funcion1squaregamut():
    t = turtle.Turtle()
    def filled_square(x,y,l):
        t.penup()
        t.goto(x,y)
        t.begin_fill()
        t.setheading(90)
        for _ in range(4):
            t.forward(l)
            t.right(90)
        t.end_fill()
    def red_gamut(x,y,r):
        for b in range(11):
            for g in range(11):
                t.color(r, g * 0.1, b * 0.1)
                filled_square(x + b * 5, y + g *5 ,5)
    def whole_gamut():
        for r in range(11):
            red_gamut(-300 + 55 * r, 0, r * 0.1)
    whole_gamut()
def funcion1AgraphPlotter():
    if len(sys.argv) < 2:
        print('No formula supplied')
        sys.exit(0)

    def plot(f):
        t = turtle.Turtle()
        t.penup()
        t.goto(-300, f(-300))
        t.pendown()
        for x in range(-300, 300, 1):
            t.goto(x, f(x))

    def farg(arg):
        def f(x): return eval(arg)
        return f

    def key(n, formula_text, color):
        t = turtle.Turtle()
        t.color(color)
        t.penup()
        t.goto(-300, -200 - 20 * n)
        t.pendown()
        t.write(formula_text, font = ("Arial", 16, "normal"))

    def line(x0, y0, x1, y1):
        t = turtle.Turtle()
        t.penup()
        t.goto(x0, y0)
        t.pendown()
        t.goto(x1, y1)

    def axes():
        t = turtle.Turtle()
        t.color("black")
        line(-300, 0, 300, 0)
        line(0, -300, 0, 300)
        for x in range(-300, 301, 50):
            if x != 0:
                t.penup()
                t.goto(x, -20)
                t.pendown()
                t.write(str(x), font = ("Arial", 12, "normal"))
                line(x, -5, x, 5)
        for y in range(-300, 301, 50):
            if y != 0:
                t.penup()
                t.goto(-20, y)
                t.pendown()
                t.write(str(y), font = ("Arial", 12, "normal"))
                line(-5, y, 5, y)
    t = turtle.Turtle()
    colors = ["black", "red", "green", "blue"]

    t.speed(0)

    axes()

    for n, arg in enumerate(sys.argv[1:]):
        t.pencolor(colors[n % 4])
        plot(farg(arg))
        key(n, arg, colors[n % 4])



def funcion1Bclock():
    t = turtle.Turtle()
    def hand(length, thickness, angle):
        t.penup()
        t.home()
        t.setheading(90)
        t.pensize(thickness)
        t.pendown()
        t.rt(angle)
        t.fd(length)
    def tickmarks():
        t = turtle.Turtle()
        t.pensize(1)
        for a in range (0, 60):
            t.penup()
            t.home()
            t.setheading(90)
            t.rt(360 / 60 * a)
            t.fd(295)
            t.pendown()
            t.fd(5)
    def clockface(h, m, s):
        t.penup()
        t.goto(0, -300)
        t.pensize(1)
        t.pendown()
        t.circle(300)
        tickmarks()
        hand(200, 3, 360 / 12 * (h % 12))
        hand(280, 3, 360 / 60 * m)
        hand(295, 1, 360 / 60 * s)
    t = turtle.Turtle()
    t.hideturtle()
    turtle.Screen().tracer(0, 0)
    while True:
        tm = time.localtime()
        t.home()
        t.clear()
        clockface(tm.tm_hour, tm.tm_min, tm.tm_sec)
        turtle.Screen().update()
        time.sleep(1)