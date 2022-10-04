import csv
import os.path

foods = ['Foods', 'Weight', 'Calories']
carrots_cooked = ['Carrots', 'Cooked', 100, 109]
carrots_raw = ['Carrots','Raw', 100, 111]
peas = ['Peas', 100, 350]

file_exists = os.path.exists('csvcals.py')

if file_exists:
    print("File already exists")
else:
    print("File does not exit. Proceeding to create a new one")
    f = open('csvcals.py', 'w')
    writer = csv.writer(f)



with open('csvcals.py','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(foods)
    writer.writerow(carrots_cooked)
    writer.writerow(carrots_raw)
    writer.writerow(peas)

with open('csvcals.py','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)