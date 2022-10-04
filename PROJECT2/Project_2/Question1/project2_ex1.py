import datetime
import os
os.system("calories.txt")
os.system("csvcals.py")

def table_of_file(filename):
    with open(filename) as f:
        table = {}
        for l in f.readlines():
            fields = l.split()
            key = fields[0]
            values = fields[1:]
            table[key] = values
        return table
#
def list_foods():
    for k, vs in table_of_file('calories.txt').items():
        print(k, end=' ')
        for v in vs: print(v, end=' ')
        print('')
#
def list_eaten(name, date):
    for k, vs in table_of_file(os.path.join(name, date)+ '.txt').items():
        print(f'{k} {vs[0]}')
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
#
def total_date(name,date):
    calories = table_of_file('calories.txt')
    table = table_of_file(os.path.join(name,date)+ '.txt')
    total = 0
    for k, vs in table.items():
        weight_and_calories = calories[k]
        reference_weight = int(weight_and_calories[0])
        reference_calories = int(weight_and_calories[1])
        calories_per_gram = reference_calories / reference_weight
        total += int(vs[0]) * calories_per_gram
    print(f'Total calories for {date}: {int(total)}')

def date_today():
    d = datetime.datetime.now()
    return f'{d.day:02}-{d.month:02}-{d.year}'

def eaten(name, food,grams):
    with open(os.path.join(name, date_today()) + '.txt', 'a') as f:
            print(f'{food} {grams}', file=f)

def weighed(name, weight):
    with open(os.path.join(name, 'weight.txt'), 'a') as f:
            print(f'{date_today()} {weight}', file=f)
#

#




