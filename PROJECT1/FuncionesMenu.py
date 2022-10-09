from Ejercicio1 import *
#from Ejercicio2 import *
#from Ejercicio3 import *
#from Ejercicio4 import *

#Opciones Menú

def Ejercicio2():
    print('Has elegido la opción 2')

def Ejercicio3():
    print('Has elegido la opción 3')

def Ejercicio4():
    print('Has elegido la opción 4')
    
def salir():
    print('Saliendo')
    
#Funciones del menú

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def mostrar_menu(opciones):
    print('Selecciona el ejercicio a ejecutar:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#Funciones Submenús Ejercicio 1

def submenuEjercicio1():
    opciones = {
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
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

#Funciones Submenús Ejercicio 2

def submenuEjercicio2():
    opciones = {
        '01': ('List Weights', funcion2listWeights),
        '02': ('List Dates', funcion2listDates),
        '03': ('Lookup Weight', funcion2lookupWeight),
        '04': ('Ejercicio 2 final', funcion2final),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

def submenuEjercicio3():
    opciones = {
        '01': ('Print Board', funcion3PrintBoard),
        '02': ('Random Move', funcion3RandomMove),
        '03': ('Human Move', funcion3HumanMove),
        '04': ('Computer Move', funcion3ComputerMove),
        
        '05': ('Human Move', funcion3HumanMove),
        '06': ('Computer Move', funcion3ComputerMove),
        '07': ('Ejercicio 2 final', funcion2final),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

def funcion2listWeights():
    print('Has elegido el Ejercicio 2 List Weights')
    
def funcion2listDates():
    print('Has elegido el Ejercicio 2 List Dates')
    
def funcion2lookupWeight():
    print('Has elegido el Ejercicio 2 Lookup Weight')
    
def funcion2final():
    print('Has elegido el Ejercicio 2 Final')
    
    generar_menu(opciones, 'b')
