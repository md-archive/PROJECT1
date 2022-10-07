import turtle
import random
import math

#INITIALISING VARIABLES

# DECLARING (MODIFIABLE) CONSTANTS

FW_1 = 50
FW_2 = 100
FW_3 = 150
# SQUARE CONSTANTS
SIDES = 4
DEGREES = 90
DISTANCE = 100
FLOWER = 10
# GENERAL ROTATION SETTING CONSTANT
ROTATION_DEGREES = 360
# GENERAL OBJECT SIZE CONSTANT 
SIZE = 100
# NUMBER OF LINES TO DRAW
LINES = 40
# POLYGON SIDES AND SIZE TO DRAW
POLYGON_SIDES = 8
POLYGON_SIZE = 100

RAD_EQ_TOTAL_SIZE = 50
STAR_QTY = 20

QTY = 20
# FUNCTIONS LIST
def funcion1square():
    t = turtle.Turtle()
    
    for _ in range(SIDES):
        t.right(DEGREES)
        t.forward(DISTANCE)
    t.home()
    t.clear()

def funcion1filledSquare():
    print('Has elegido el Ejercicio 1 Filled Square')
    
def funcion1multiSquare():
    print('Has elegido el Ejercicio 1 MultiSquare')

def funcion1polygon():
    t = turtle.Turtle()
    for _ in range(POLYGON_SIDES):
        t.forward(POLYGON_SIZE) 
        t.right(DEGREES)
    
def funcion1circle():
    t = turtle.Turtle()
    total = 0
    t.setposition(0,0)   
    total = 2 * math.pi * RAD_EQ_TOTAL_SIZE
    num = int(total)
    for _ in range(num):
        t.forward(1.5)
        t.left(1.15)
    t.home()
    t.clear()
    
def funcion1filledCircle():
    print('Has elegido el Ejercicio 1 Filled Circle')
    
def funcion1squareCircles():
    print('Has elegido el Ejercicio 1 Square Circles')
    
def funcion1star():
    print("HOLA|HALLO|HEI")    

def funcion1stars():
    t=turtle.Turtle()
    
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
        funcion1stars(random.randint(-300,300),
            random.randint(-300,300),
            random.randint(10,150),
            random.randint(3,30)) 
    
def funcion1AgraphPlotter():
    print('Has elegido el Ejercicio 1A Graph Plotter')
    
def funcion1Bclock():
    print('Has elegido el Ejercicio 1A Clock')    