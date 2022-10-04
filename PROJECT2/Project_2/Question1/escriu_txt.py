import os.path

carrots = ['Carrots',160]
peas = ['Peas',110]

file_exists = os.path.exists('calories.txt')

if file_exists:
    print("File already exists")
else:
    print("File does not exit. Proceeding to create a new one")
    f = open('calories.txt', 'x')

with open('calories.txt', 'w', encoding='UTF8', newline='') as f:
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