import csv
import os
import datetime
import sys
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 0.1 : LEER FICHERO CALORIES.TXT E ITERAR SUS FILERAS -> 1ra manera
    #
    # -------------------------------------------------------------
    #
    # fields guarda una filera entera
    # La llave será la primera posición
    # Los valores estarán después de la llave
    # La table equivaldrá a la lectura del fichero entero
    #
def table_of_file(filename):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'calories.txt')
    with open(filename) as row:
        table = {}
        for cursor in row.readlines():
            fields = cursor.split()
            key = fields[0]
            values = fields[1:]
            table[key] = values
        return table
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 0.2 : LEER FICHERO CALORIES.TXT Y MOSTRAR OUTPUT AMIGABLE (sin simbolos)
    #
    # -------------------------------------------------------------
    #
def list_foods(filename):
    for llaves, vs in table_of_file(filename).items():
        # claus
        print(llaves, end=' ')
        # valors
        for valores in vs: print(valores, end=' ')
        print('\n')
list_foods('calories.txt')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 0.3 : LEER FICHERO DE LOS USUARIOS CON SU RESPECTIVA FECHA
    #
    # -------------------------------------------------------------
    #
def list_eaten(name, date):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name, date))
    for llaves, vs in table_of_file(filename + '.txt').items():
        print(f'{llaves} {vs[0]}')
list_eaten('robert','01-01-2020.txt')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 1 : LISTAR CONTENIDO DEL FICHERO "weight.txt" de un usuario
    #
    # -------------------------------------------------------------
    #
def list_weights(name):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name))
    for cursor, vs in table_of_file(os.path.join(filename, 'weight.txt')).items():
        print(f'{cursor} {vs[0]}')
list_weights('robert')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 2.1 : LISTAR FICHEROS DE LA CARPETA DEL USUARIO
    #
    # -------------------------------------------------------------
    #
def list_dates(name):
    for filename in sorted(os.listdir(name)):
        if filename != 'weight.txt': print(filename[:-4])
list_dates('mary')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 2.2 : LISTAR CALORIAS DE UNA COMIDA EN "calories.txt"
    #
    # -------------------------------------------------------------
    #
def lookup_calories(food):
    table = table_of_file('calories.txt')
    vs = table[food]
    if vs is None:
        print(f'Food {food} not found')
    else:
        if len(vs) > 1:
            weight = vs[0]
            calories = vs[1]
            print(f'There are {calories} calories in {weight}g of {food}')
        else:
            print(f'Malformed calorie entry for {food} in calories file')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 3 : PESO DEL USUARIO EN ESA FECHA
    #
    # -------------------------------------------------------------
    #
def total_date(name, date):
    calories = table_of_file('calories.txt')
    table = table_of_file(os.path.join(name, date) + '.txt')
    total = 0
    for k, vs in table.items():
        weight_and_calories = calories[k]
        reference_weight = int(weight_and_calories[0])
        reference_calories = int(weight_and_calories[1])
        calories_per_gram = reference_calories / reference_weight
        total += int(vs[0]) * calories_per_gram
    print(f'Total calories for {date}: {int(total)}')
# total_date('robert','01-01-2020.txt')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 4.1 : ESTRUCTURA PARA UN NUEVO USUARIO
    #
    # -------------------------------------------------------------
    #
    input(name)
def new_user(name):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name))
    # Si no existe el directorio del usuario -> Crealo
    if(name == False):
        os.mkdir(filename)
    else:
        print(f'Directory {name} already registered.')
    with open(os.path.join(filename, 'weight.txt'), 'w') as f:
        print('Date,Weight', file=f)

    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 4.2 : FECHA DE CALORIAS ACORDE AL NTP DEL PC
    #
    # -------------------------------------------------------------
    #
def date_today():
    fecha = datetime.datetime.now()
    full_date = (f'{fecha.day:02}-{fecha.month:02}-{fecha.year}')
    print(full_date)
    return full_date
date_today()
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 4.3 : CREAR FICHEROS 'weight.txt' y 'calories.txt' acorde al usuario
    #
    # -------------------------------------------------------------
    #
def eaten(name, food, grams):
    with open(os.path.join(name, date_today()) + '.txt', 'a') as f:
        print(f'{food} {grams}', file=f)
#
eaten('robert',"'Peas':",'450')
#
def weighed(name, weight):
    with open(os.path.join(name, 'weight.txt'), 'a') as f:
        print(f'{date_today()} {weight}', file=f)
weighed('robert','80')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 4.4 : TYPE DATA FROM THE COMMAND LINE
    #
    # -------------------------------------------------------------
    #
def lookup_weight(name, date):
    table = table_of_file(os.path.join(name, 'weight.txt'))
    vs = table[date]
    if vs is None:
        print(f'No weight found for {date}')
    elif len(vs) > 0:
        print(f'Weight at {date} was {vs[0]}')

input("Write Command and Descritpion: ").split()
def total_date(name, date):
    calories = table_of_file('calories.txt')
    table = table_of_file(os.path.join(name, date) + '.txt')
    total = 0
    for k, vs in table.items():
        weight_and_calories = calories[k]
        reference_weight = int(weight_and_calories[0])
        reference_calories = int(weight_and_calories[1])
        calories_per_gram = reference_calories / reference_weight
        total += int(vs[0]) * calories_per_gram
    print(f'Total calories for {date}: {int(total)}')

arg = sys.argv
print ("This is the name of the script: ", sys.argv[1])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
if len(arg) > 1:
    cmd = arg[1]
    if cmd == 'list':
        if len(arg) > 3 and arg[2] == 'eaten':
            list_eaten(arg[3], arg[4])
        else:
            if arg[2] == 'weights' and len(arg) > 3:
                list_weights(arg[3])
            elif arg[2] == 'dates' and len(arg) > 3:
                list_dates(arg[3])
            elif arg[2] == 'foods':
                list_foods()
    elif cmd == 'lookup':
        if len(arg) > 2:
            if arg[2] == 'calories':
                lookup_calories(arg[3])
            elif arg[2] == 'weight' and len(arg) > 3:
                lookup_weight(arg[3], arg[4])
    elif cmd == 'total':
        if len(arg) > 3:
            total_date(arg[2], arg[3])
    elif cmd == 'newuser':
        if len(arg) > 2:
            new_user(arg[2])
    elif cmd == 'eaten':
        if len(arg) > 4:
            eaten(arg[2], arg[3], arg[4])
    elif cmd == 'weighed':
        if len(arg) > 3:
            weighed(arg[2], arg[3])
    else:
        print('Command not understood')
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 5.1 : CONTROL DE ERRORES EN LOS INPUTS (no solución en documentación)
    #
    # -------------------------------------------------------------
    #
    #
    # -------------------------------------------------------------
    #
    # EJERCICIO 5.2 : CONTROL DE ERRORES EN LOS INPUTS (no solución en documentación)
    #
    # -------------------------------------------------------------
    #