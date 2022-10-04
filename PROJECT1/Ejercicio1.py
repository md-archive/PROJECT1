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



def funcion1square():
        for _ in range(4):
                t.fd(x)
                t.rt(90)
for _ in range(10):
        funcion1square(100)
        t.rt(360/10)
    
def funcion1filledSquare():
    print('Has elegido el Ejercicio 1 Filled Square')
    
def funcion1multiSquare():
    print('Has elegido el Ejercicio 1 MultiSquare')
  
def funcion1polygon(l, n):
   for i in range(7):
      t.forward(l) 
      t.right(n)
funcion1polygon(100, 51.6)

def funcion1circle():
    print('Has elegido el Ejercicio 1 Circle')
    
def funcion1filledCircle():
    print('Has elegido el Ejercicio 1 Filled Circle')
    
def funcion1squareCircles():
    print('Has elegido el Ejercicio 1 Square Circles')
    
def funcion1star(l, n):
        for _ in range(n):
                t.fd(l)
                t.bk(l)
                t.rt(360/n)
        funcion1star(100, 20)

def funcion1stars(x, y, l, n):
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
    funcion1stars(random.randint(-300, 300),
         random.randint(-300, 300),
         random.randint(10, 150),
         random.randint(3, 30))

    
def funcion1AgraphPlotter():
    print('Has elegido el Ejercicio 1A Graph Plotter')
    
def funcion1Bclock():
    print('Has elegido el Ejercicio 1A Clock')