from FuncionesMenu import *

def initial_menu():
    options= {
        '1': ('Ejercicio 1', submenuEjercicio1),
        '2': ('Ejercicio 2', submenuEjercicio2),
        '3': ('Ejercicio 3', Ejercicio3),
        '4': ('Ejercicio 4', Ejercicio4),
        's': ('Salir', salir)
    }
    generate_menu(options, 's')  #Generamos el menú hasta que se introduzca la s


initial_menu() #Arranque programa