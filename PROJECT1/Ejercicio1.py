import turtle
import random
import math
#
t_inv = turtle.Turtle()
#
sides = 4
degrees = 90
distance = 100
flower = 10
#
circle_degrees = 360
#
size = 100
lines = 40
#
polygon_sides = 8
#
rad_eq_total_size = 50
#
star_quantity = 20
#
def func_square():
        for _ in range(sides):
                t_inv.right(degrees)
                t_inv.forward(distance)
func_square()
#
def funcion1square():
        for _ in range(sides):
                t_inv.forward(distance)
                t_inv.right(degrees)
#
for _ in range(flower):
        funcion1square(distance)
        t_inv.right(circle_degrees/flower)

def funcion1star(size, lines):
        for _ in range(lines):
                t_inv.forward(size)
                t_inv.back(size)
                t_inv.right(circle_degrees/lines)
        funcion1star(size, lines)

def funcion1polygon(polygon_size):
   for _ in range(polygon_sides):
      t_inv.forward(polygon_size) 
      t_inv.right(degrees)
funcion1polygon(100)

def funcion1circle():
     total = 0
     t_inv.setposition(0,0)   
     total = 2 * math.pi * rad_eq_total_size
     num = int(total)
     for _ in range(num):
        t_inv.forward(1.5)
        t_inv.left(1.15)

def funcion1stars(drw_forw,draw_forw2,drw_forw3,num_lines):
    t_inv.penup()
    t_inv.home()
    t_inv.forward(drw_forw)
    t_inv.left(left_degrees)
    t_inv.forward(draw_forw2)
    t_inv.pendown()
    for _ in range(num_lines):
        t_inv.forward(drw_forw3)
        t_inv.back(drw_forw3)
        t_inv.right(degrees/num_lines)
# randint = Random star position
# number shows where the turtle will be displayed
#
for _ in range(star_quantity):
    left_degrees = 90
    funcion1stars(random.randint(-300,300),
        random.randint(-300,300),
        random.randint(10,150),
        random.randint(3,30)) 

degrees=360
#
quantity = 20
#
def funcion1starfilled(drw_forw,draw_forw2,drw_forw3,num_lines):
    t_inv.penup()
    t_inv.goto(drw_forw,draw_forw2)
    t_inv.pendown()
    for _ in range(num_lines):
        t_inv.forward(drw_forw3)
        t_inv.back(drw_forw3)
        t_inv.right(degrees/num_lines)
#
t_inv.hideturtle()
t_inv.speed(8)
funcion1starfilled(10,10,200,7)
t_inv.showturtle()
#
t_inv.pensize(20)
funcion1starfilled(0, 0, 200, 7)
t_inv.pensize(15)
t_inv.color(0.25, 0.25, 0.25)
funcion1starfilled(0, 0, 200, 7)
t_inv.pensize(10)
t_inv.color(0.5, 0.5, 0.5)
funcion1starfilled(0, 0, 200, 7)
t_inv.pensize(5)
t_inv.color(0.75, 0.75, 0.75)
funcion1starfilled(0, 0, 200, 7)
t_inv.pensize(2)
t_inv.color(1, 1, 1)
funcion1starfilled(0, 0, 200, 7)
t_inv.hideturtle()


def funcion1filledSquare():
    print('Has elegido el Ejercicio 1 Filled Square')
    
def funcion1multiSquare():
    print('Has elegido el Ejercicio 1 MultiSquare')
  
def funcion1filledCircle():
    print('Has elegido el Ejercicio 1 Filled Circle')
    
def funcion1squareCircles():
    print('Has elegido el Ejercicio 1 Square Circles')  
    
def funcion1AgraphPlotter():
    print('Has elegido el Ejercicio 1A Graph Plotter')
    
def funcion1Bclock():
    print('Has elegido el Ejercicio 1A Clock')