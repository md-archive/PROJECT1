import os.path

carrots = ['Carrots',160]
peas = ['Peas',110]

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'calories.txt')
file_exists = os.path.exists(filename)

if file_exists == True:
    print("File already exists")
else:
    print("File does not exit. Proceeding to create a new one")
    f = open('calories.txt', 'a').close()

with open(filename, 'w', encoding='UTF8', newline='') as f:
    for line in carrots:
        if type(line) is int:
            f.write(" " + str(line) + "\n")
        else:
            f.write(line)
    for line in peas:
        if type(line) is int:
            f.write(" " + str(line) + "\n")
        else:
            f.write(line)