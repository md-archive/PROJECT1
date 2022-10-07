from FuncionesMenu import *

def menu_principal():
    opciones = {
        '1': ('Ejercicio 1', submenuEjercicio1),
        '2': ('Ejercicio 2', submenuEjercicio2),
        '3': ('Ejercicio 3', Ejercicio3),
        '4': ('Ejercicio 4', Ejercicio4),
        's': ('Salir', salir)
    }

    generar_menu(opciones, 's')  #Generamos el menú hasta que se introduzca la s


menu_principal() #Arranque programa