import datetime
import sys
import os
import csv
import re
def table_of_file(filename):
    # dirname = os.path.dirname(__file__)
    # filename = os.path.join(dirname, 'calories.txt')
    try:            # %%% Si el usuario introduce una fecha no valida %%%
        with open(filename) as row:
            table = {}  
            for cursor in row.readlines():
                fields = cursor.split()
                key = fields[0]
                values = fields[1:]
                table[key] = values
                    #print(f'{key[0:]} {values[0]} {values[1]} {values[2]} {values[3]}')
                if len(values) == 3:
                    print(f'{key[0:]} {values[0]} {values[1]} {values[2]}')
                if len(values) == 4:
                    print(f'{key[0:]} {values[0]} {values[1]} {values[2]} {values[3]}')
            if len(table) == 0:
                print("ERROR! File was found, but no data on it.")
                #print("Add new food by typing your name, that food and its weight.\n")
            else:
                print("\n")
            return table
    except:
        print("ERROR!! File is not found. Have you already created?")

# def table_of_file(filename):
#     with open(filename) as c:
#         r = csv.reader(c)
#         next(r)
#         table = {}
#         for row in r:
#             table[row[0]] = row[1:]
#         return table 

def list_eaten(name,date):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name, date + '.txt'))
    table_of_file(filename)


def list_weights(name):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name,'weight.txt'))
    table_of_file(filename)
    # for cursor, vs in table_of_file(os.path.join(filename)).items():
    #     print(f'{cursor} {vs[0]}')

def list_dates(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,name)
    try:
        sort_filename = os.listdir(filename)
        for filename in sorted(sort_filename):
            if filename != 'weight.txt': print(filename[:-3])
        print("\n")
    except:
        print(f"{name}'s is not registered. Is this user created?")


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
    print("\n")
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
                        print(f'There are {valores[0]} calories in {weight[1]}g of {llaves}')
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
            #print(f'There are {calories} calories in {weight}g of {food}')
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
    filename = os.path.join(dirname, 'calories.txt')
    calories = table_of_file(filename)
    table = table_of_file(os.path.join(filename, name, date) + '.txt')
    total = 0
    for key, vs in table.items():
        for ch in ["{","'",":"]:
            if ch in key:
                key = key.replace(ch,"")
        for valores in vs: 
            for ch in ["[","'","]",",","}"]:
                if ch in valores:
                    valores = valores.replace(ch,"")
            print(valores, end=' ')
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
    is_new = not os.path.exists(filename)
    with open(os.path.join(filename, date_today()) + '.txt', 'a') as f:
        if is_new: print('Food,Weight', file=f)
        print(f'Food selected : {food} \n Current food weightttttttt : {food_weight}g' , file=f)
#

def weighed(name, person_weight):
    dirname = os.path.dirname(__file__)
    filename = (os.path.join(dirname,name,'weight.txt'))
    is_new = not os.path.exists(filename)
    with open(filename, 'a') as f:
        if is_new: print('Date,Weight', file=f)
        print(f"Date registered : {date_today()} \n Current {name}'s weight : {person_weight} Kg", file=f)

def date_today():
    fecha = datetime.datetime.now()
    full_date = (f'{fecha.day:01}-{fecha.month:01}-{fecha.year}')
    print(full_date)
    return full_date

# arg = sys.argv
print("_______________________________________________________________________________")
print("\n    <-- Command  -->                 <-- Description  -->  ")
print("-------------------------------------------------------------------------------")
print("list eaten <name> <date>      List foods eaten on a given date.")
print("list weights <name>           List the weight history for a user.")
print("list dates <name>             List the dates for which there are calorie counts.")
print("list foods                    List all calorie data for known foods.")
print("lookup calories <food>        Lookup up calories for a given food.")
print("lookup weight <name> <date>   Lookup up weight for given date")
print("total <name> <date>           Calculate total calories for a given user and date.")
print("newuser <name>                Create a new user.")
print("eaten <name> <food> <weight>  Add food data for today.")
print("weighed <name> <weight>       Add weight data for today.\n")
print("-------------------------------------------------------------------------------")
print("Write your name in lower case [a-z]")
print("Format date should be this one : '%d-%m-%Y'")
print("-------------------------------------------------------------------------------\n")
arg = input("Write Command and Description: ").split()

if len(arg) > 0:
    cmd = arg[0]
    if len(arg) > 1:
        if cmd == 'list':
            if len(arg) > 2 and arg[1] == 'eaten':
                if len(arg) == 4:
                    if re.search("[a-z]$", arg[2]):
                        try:
                            date_format = datetime.datetime.strptime(arg[3],'%d-%m-%Y')
                            print("\n-----------------------------------------------")
                            print(f"Consulting {arg[2]}'s foods eaten on {arg[3]}.")
                            print("-----------------------------------------------\n")
                            list_eaten(arg[2], arg[3])
                        except:
                            print("ERROR! Mismatched format date, should be this one : '%d-%m-%Y'")
                    else:
                        print("ERROR! 3rd parameter must be a name")
                else:
                    print("ERROR! Not enough, to many or wrong parameters for listing foods from a user on a given day.")
                    print("Correct format : list eaten <name> <date>")
            else:
                if arg[1] == 'weights' and len(arg) > 2:
                    if len(arg) == 3:
                        if re.search("[a-z]$", arg[2]):
                            print("\n-----------------------------------------------")
                            print(f"Consulting {arg[2]}'s weights.")
                            print("-----------------------------------------------\n")
                            list_weights(arg[2])
                        else:
                            print("ERROR! 3rd parameter must be a name")
                    else:
                        print("ERROR! Not enough, to many or wrong parameters for listing weight from a given user.")
                        print("Correct format : list weights <name>")
                elif arg[1] == 'dates' and len(arg) > 2:
                    if len(arg) == 3:
                        if re.search("[a-z]$", arg[2]):
                            print("\n-----------------------------------------------")
                            print(f"Consulting {arg[2]}'s dates from calorie registration.")
                            print("-----------------------------------------------\n")
                            list_dates(arg[2])
                        else:
                            print("ERROR! 3rd parameter must be a name")
                    else:
                        print("ERROR! Not enough, to many or wrong parameters for listing dates from a given user.")
                        print("Correct format : list dates <name>")
                elif arg[1] == 'foods':
                    if len(arg) == 2:
                        print("\n-----------------------------------------------")
                        print(f"These are the foods available to register for your user.")
                        print("-----------------------------------------------")
                        list_foods()
                    else:
                        print("ERROR! Not enough or to many parameters for listing foods on a given day.")
                else:
                    print("Missing parameters. Are 'name' and 'date' both mentioned?")
                    print("Correct format : list eaten <name> <date>")
        elif cmd == 'lookup':
            if len(arg) > 1:
                if arg[1] == 'calories':
                    if len(arg) == 3:
                        lookup_calories(arg[2])
                    elif len(arg) == 2:
                        print("ERROR! Is the food mentioned?")
                        print("Correct format : lookup calories <food>")
                    else:
                        print("ERROR! Not enough or to many parameters for listing foods on a given day.")
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
    else:
        print("ERROR!! At least 2 parameters are required.")
