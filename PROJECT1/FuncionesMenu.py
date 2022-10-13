from Ejercicio1 import *
from Ejercicio2 import *
#from Ejercicio3 import *
from Ejercicio4 import *
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
        opcion = leer_opcion(opcion, opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def mostrar_menu(opciones):
    print('Selecciona el ejercicio a ejecutar:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

'''
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
'''
def leer_opcion(opcion, opciones):
    opcion = input('Opción: ')
    alternativas = ['1','2','3','4','5','6','7','8','9','10','11','B','S']
    if '01' in opciones:
        if opcion !=10 or opcion !=11 :
            opcion = '0' + opcion
        elif opcion == 'B' or opcion == 'S':
            opcion = input.lower()
   
    while opcion not in opciones:
        verificar_input(opcion, opciones)

    return opcion

def verificar_input(opcion, opciones):
    if opcion not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
        leer_opcion(opcion, opciones)

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
        '10': ('Opción Grid Circles', funcion1gridcircles),
        '10': ('Opción Square Gamut', funcion1squaregamut),
        '11': ('Opción Agraph Plotter', funcion1AgraphPlotter),
        '12': ('Opción Clock', funcion1Bclock),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

#Funciones Submenús Ejercicio 2

def submenuEjercicio2():
    opciones = {
        '01': ('List Weights', list_weights),
        '02': ('List Dates', list_dates),
        '03': ('Lookup Weight', lookup_weight),
        '04': ('New User', new_user),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

def submenuEjercicio3():
    opciones = {
        '01': ('Print Board', funcion3PrintBoard),
        '02': ('Random Move', funcion3RandomMove),
        '03': ('Human Move', funcion3HumanMove),
        '04': ('Computer Move', funcion3ComputerMove),
        '05': ('Swap Player', funcion3SwapPlayer),
        '06': ('Next Board', funcion3NextBoard),
        '07': ('Sum X Wins', funcion3SumXWins),
        '08': ('Ejercicio 3 final', funcion3final),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')

def submenuEjercicio4():
    opciones = {
        '01': ('Black and White (1st way)', funcion4BlackandWhite_1),
        '02': ('Black and White (2nd way)', funcion4BlackandWhite_2),
        '02': ('Pixels in place', funcion4ProcessPixelsInPlace),
        '03': ('Flip Image', funcion4FlipImage),
        '04': ('Image Border', funcion4Border),
        '05': ('Process Pixels', funcion4Fade_1),
        '06': ('GIF Fade', funcion4Fade_2),
        '07': ('Make Images', funcion4MakeImages),
        '08': ('Ejercicio 3 final', funcion4final),
        'b': ('Volver al menú principal', salir)
    }

    generar_menu(opciones, 'b')
'''
def funcion2listWeights():
    print('Has elegido el Ejercicio 2 List Weights')
    
def funcion2listDates():
    print('Has elegido el Ejercicio 2 List Dates')
    
def funcion2lookupWeight():
    print('Has elegido el Ejercicio 2 Lookup Weight')
    
def funcion2final():
    print('Has elegido el Ejercicio 2 Final')
    
    generar_menu(opciones, 'b')
'''
