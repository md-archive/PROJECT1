import datetime
import sys
import os
import csv

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

def list_eaten(name,date):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name, date + '.txt'))
    for llaves, vs in table_of_file(filename).items():
        print(f'{llaves} {vs[0]}')

def list_weights(name):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name,'weight.txt'))
    for cursor, vs in table_of_file(os.path.join(filename)).items():
        print(f'{cursor} {vs[0]}')

def list_dates(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,name)
    for filename in sorted(os.listdir(filename)):
        if filename != 'weight.txt': print(filename[:-3])

def list_foods():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'calories.txt')
    for llaves, vs in table_of_file(filename).items():
        for ch in ["{","'",":"]:
            if ch in llaves:
                llaves = llaves.replace(ch,"")
        # x = llaves.replace("{","")
        # y = llaves.replace("'","")
        # z = llaves.replace(":","")
        # full_key = x + y + z
        # claus
        print(llaves, end=' ')
        # valors
        for valores in vs: 
            for ch in ["[","'","]",",","}"]:
                if ch in valores:
                    valores = valores.replace(ch,"")
            print(valores, end=' ')
        print('')

def lookup_calories(food):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'calories.txt')
    # table = table_of_file(filename)
    #
    for llaves, vs in table_of_file(filename).items():
        for ch in ["{","'",":"]:
            if ch in llaves:
                llaves = llaves.replace(ch,"")
                if llaves == food:
                    print(llaves, end=' ')
                    for valores in vs: 
                        for ch in ["[","'","]",",","}"]:
                            if ch in valores:
                                valores = valores.replace(ch,"")
                        print(valores, end=' ')
        # x = llaves.replace("{","")
        # y = llaves.replace("'","")
        # z = llaves.replace(":","")
        # full_key = x + y + z
        # claus
 
        # valors
        
    
    #vs = table[food]
    if vs is None:
        print(f'Food {food} not found')
    else:
        if len(vs) > 0:
            weight = vs[0]
            calories = vs[0]
            print(f'There are {calories} calories in {weight}g of {food}')
        else:
            print(f'Malformed calorie entry for {food} in calories file')

def lookup_weight(name, date):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,name, 'weight.txt')
    table = table_of_file(filename)
    vs = table[date]
    if vs is None:
        print(f'No weight found for {date}')
    elif len(vs) > 0:
        print(f'Weight at {date} was {vs[0]}')

def total_date(name, date):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,name, 'calories.txt')
    calories = table_of_file(filename)
    table = table_of_file(os.path.join(filename, name, date) + '.txt')
    total = 0
    for key, vs in table.items():
        weight_and_calories = calories[key]
        reference_weight = int(weight_and_calories[0])
        reference_calories = int(weight_and_calories[0])
        calories_per_gram = reference_calories / reference_weight
        total += int(vs[0]) * calories_per_gram
    print(f'Total calories for {date}: {int(total)}')

def new_user(name):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name))
    directory_exists = os.path.exists(filename)
    # Si no existe el directorio del usuario -> Crealo
    if(directory_exists == False):
        os.mkdir(filename)
    else:
        print(f'Directory {name} already registered.')
    # Si el directorio existe, sobreescribe el contenido del fichero
    with open(os.path.join(filename, 'weight.txt'), 'w') as f:
        print('Date,Weight', file=f)

def eaten(name, food, food_weight):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name))
    with open(os.path.join(filename, date_today()) + '.txt', 'a') as f:
        print(f'Food selected : {food} \n Current weight : {food_weight}', file=f)
#

def weighed(name, person_weight):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name))
    with open(os.path.join(filename, 'weight.txt'), 'a') as f:
        print(f'Date registered : {date_today()} \n Current weight : {person_weight}', file=f)

def date_today():
    fecha = datetime.datetime.now()
    full_date = (f'{fecha.day:01}-{fecha.month:01}-{fecha.year}')
    print(full_date)
    return full_date

# arg = sys.argv

arg = input("Write Command and Descritpion: ").split()

if len(arg) > 0:
    cmd = arg[0]
    if cmd == 'list':
        if len(arg) > 2 and arg[1] == 'eaten':
            list_eaten(arg[2], arg[3])
        else:
            if arg[1] == 'weights' and len(arg) > 2:
                list_weights(arg[2])
            elif arg[1] == 'dates' and len(arg) > 2:
                list_dates(arg[2])
            elif arg[1] == 'foods':
                list_foods()
            else:
                print("Missing parameters. Are 'name' and 'date' both mentioned?")
            
    elif cmd == 'lookup':
        if len(arg) > 1:
            if arg[1] == 'calories':
                lookup_calories(arg[2])
            elif arg[1] == 'weight' and len(arg) > 2:
                lookup_weight(arg[2], arg[3])
            else:
                print("Missing parameters. Are 'calories' and 'weight' both mentioned?")
    elif cmd == 'total':
        if len(arg) > 2:
            total_date(arg[1], arg[2])
        else:
            print("Missing parameters. Are 'name' and 'date' both mentioned?")
    elif cmd == 'newuser':
        if len(arg) > 1:
            new_user(arg[1])
        else:
            print("Missing parameter. Is the 'name' of the user mentioned?")
    elif cmd == 'eaten':
        if len(arg) > 3:
            eaten(arg[1], arg[2], arg[3])
        else:
            print("Missing parameters. Are the 'name', 'food' and 'weight' all of them mentioned?")
    elif cmd == 'weighed':
        if len(arg) > 2:
            weighed(arg[1], arg[2])
        else:
            print("Missing parameters. Are the 'name' and 'weight' both mentioned?")
    else:
        print('Command not understood')