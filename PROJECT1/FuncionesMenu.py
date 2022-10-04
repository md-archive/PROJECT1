from tkinter import N
from Ejercicio1 import *
from Ejercicio2 import *
from Ejercicio3 import *
from Ejercicio4 import *

#Opciones Menú
def Ejercicio1():
    print("Hi")
def Ejercicio2():
    print('Has elegido la opción 2')


def Ejercicio3():
    print('Has elegido la opción 3')


def Ejercicio4():
    print('Has elegido la opción 4')
    
def salir():
    print('Saliendo')
    
#Funciones del menú

def generate_menu(options, exit_opts):
    option = None
    while option != exit_opts:
        show_menu(options)
        option = read_option(options)
        execute_options(option,options)
        print()
    
def show_menu(options):
    print('Choose an exercise to run:')
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')


def read_option(options):
    while (a := input('Option: ').lower()) not in options:
        print('Wrong choice, try again!')        
    return a


def execute_options(option, options):
    options[option][1]()

#Funciones Submenús Ejercicio 1

def submenuEjercicio1():
    options = {
        '01': ('Opción Square', funcion1square),
        '02': ('Opción Filled Square', funcion1filledSquare),
        '03': ('Opción Multi Square', funcion1multiSquare),
        '04': ('Opción Polygon', funcion1polygon),
        '05': ('Opción Circle', funcion1circle),
        '06': ('Opción Filled Circle', funcion1filledCircle),
        '07': ('Opción Square Circles', funcion1squareCircles),
        '08': ('Opción Star', funcion1star),
        '09': ('Opción Stars', funcion1stars),
        '10': ('Opción Agraph Plotter', funcion1AgraphPlotter),
        '11': ('Opción Clock', funcion1Bclock),
        '12': ('Opción estrella rellenada', funcion1starfilled),
        'b': ('Volver al menú principal', salir)
    }

    generate_menu(options, 'b')


#Funciones Submenús Ejercicio 2

def submenuEjercicio2():
    options = {
        '01': ('List Weights', funcion2listWeights),
        '02': ('List Dates', funcion2listDates),
        '03': ('Lookup Weight', funcion2lookupWeight),
        '04': ('Ejercicio 2 final', funcion2final),
        'b': ('Volver al menú principal', salir)
    }

    generate_menu(options, 'b')

def funcion2listWeights():
    print('Has elegido el Ejercicio 2 List Weights')
    
def funcion2listDates():
    print('Has elegido el Ejercicio 2 List Dates')
    
def funcion2lookupWeight():
    print('Has elegido el Ejercicio 2 Lookup Weight')
    
def funcion2final():
    print('Has elegido el Ejercicio 2 Final')
    
