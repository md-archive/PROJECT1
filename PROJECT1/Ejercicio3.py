# !/usr/bin/python3
# coding: utf-8
import random

# Reglas del juego
missatge = "Las reglas para empezar a jugar son simples, cada jugador coloca \
        por turno su 'X' o su 'O' en una de las casillas vacias, hasta que uno\
        de los dos jugadores consiga 3 de sus fichas en linea recta o en\
        horizontal"

i = 0
emptyboard = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
b = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
h1 = [0, 1, 2]
h2 = [3, 4, 5]
h3 = [6, 7, 8]
v1 = [0, 3, 6]
v2 = [1, 4, 7]
v3 = [2, 5, 8]
d1 = [0, 4, 8]
d2 = [2, 4, 6]
lines = [h1, h2, h3, v1, v2, v3, d1, d2]
NumeroRandom = random.randint(0, 8)

intersecting_lines = [(h1, v1, 0), (h1, v2, 1), (h1, v3, 2), (h2, v1, 3),
                      (h2, v2, 4), (h2, v3, 5), (h3, v1, 6), (h3, v2, 7),
                      (h3, v3, 8), (d1, h1, 0), (d1, h2, 4), (d1, h3, 8),
                      (d1, v1, 0), (d1, v2, 4), (d1, v3, 8), (d2, h1, 2),
                      (d2, h2, 4), (d2, h3, 6), (d2, v1, 2), (d2, v2, 4),
                      (d2, v3, 6), (d1, d2, 4)]
pl = '0'
pl2 = 'X'

tree = ('?',
           ('E',
               ('I',
                   ('S',
                       ('H', '5', '4'),
                       ('V', '?', '3')),
               ('U',
                   'F',
                       ('?', '?', '2'))),
                ('A',
                    ('R', 'L', '?'),
                    ('W', 'P',
                        ('J', '?', '1')))),
            ('T',
                ('N',
                    ('D',
                        ('B', '6', '?'), 'X'),
                    ('K', 'C', 'Y')),
                ('M',
                    ('G',
                        ('Z', '7', '?'), 'Q'),
                    ('O',
                        ('?', '8', '?'), ('?', '9', '0')))))

def print_board(b):
    for n, x in enumerate(b):
        print(x, end='')
        if n == 2:
            print('  012')
        elif n == 5:
            print('  345')
        elif n == 8:
            print('  678\n')


def instructions():
    print('Board is numbered\n012\n345\n678')


def full(b):
    return '_' not in b


def wins(p, b):
    win = [p, p, p]
    for ll in lines:
        bl = [b[x] for x in ll]
        if bl == win:
            return True
    return False


# Question 3
def random_play(pl, b):
    p = random.randint(0, 8)
    while b[p] != '_':
        p = (p + 1) % 9
    b[p] = pl

# Dos Maquinas


def random_game():
    b = emptyboard.copy()
    pl = '0'
    while not (full(b) or wins('X', b) or wins('0', b)):
        print_board(b)
        print("\n--------------------")
        random_play(pl, b)
        if pl == '0':
            pl = 'X'
        else:
            pl = '0'
    print_board(b)
    print("\n--------------------")
    print('Game over. Result:')
    if wins('0', b):
        print('0 wins!')
    elif wins('X', b):
        print('X wins!')
    else:
        print('Any!')

# Una Maquina


def random_game_1():
    b = emptyboard.copy()
    pl = 'X'
    while not (full(b) or wins('X', b)):
        print_board(b)
        print("\n--------------------")
        random_play(pl, b)
    print_board(b)
    print("\n--------------------")
    print('Game over. Result:')
    if wins('X', b):
        print('X wins!')
    else:
        print('Any!')

# Question 4

# Question 5


def try_to_take(b, ps):
    for p in ps:
        if b[p] == '_':
            b[p] = 'X'
            return True
    return False


def tactic_play_centre(b):
    return try_to_take(b, [4])


def tactic_first_blank(b):
    return try_to_take(b, [0, 1, 2, 3, 4, 5, 6, 7, 8])


def win_or_block(b, piece):
    for ll in lines:
        bl = [b[x] for x in ll]
        if bl.count('_') == 1 and bl.count(piece) == 2:
            for x in ll:
                if b[x] == '_':
                    b[x] = 'X'
            return True
    return False


def tactic_win(b):
    return win_or_block(b, 'X')


def tactic_block(b):
    return win_or_block(b, '0')


def human_move(pl, board):
    n_input = input('\nPosition 0..8? ')
    # print(pl)
    if n_input.isdigit():
        n = int(n_input)
        if n < 0 or n > 8:
            print('Board position must be from 0..8 ')
            human_move(pl, board)
        else:
            if board[n] != '_':
                print('Position already taken')
                human_move(pl, board)
            else:
                board[n] = pl
    else:
        print('Not a valid board position')
        human_move(pl, board)

# Question 6


def tactic_empty_corner(b):
    return try_to_take(b, [0, 2, 6, 8])


def tactic_empty_side(b):
    return try_to_take(b, [1, 3, 5, 7])


def tactic_play_opposite_corner(b):
    if b[0] == 'X':
        if try_to_take(b, [8]):
            return True
    elif b[2] == 'X':
        if try_to_take(b, [6]):
            return True
    elif b[6] == 'X':
        if try_to_take(b, [2]):
            return True
    elif b[8] == 'X':
        return try_to_take(b, 0)


def computer_move(b):
    print('\nComputer has played:')
    if tactic_win(b):
        print('Used tactic_win')
        return
    if tactic_block(b):
        print('Used tactic_block')
        return
    if tactic_play_centre(b):
        print('Used tactic_centre')
        return
    if tactic_play_opposite_corner(b):
        print('Used  tactic_play_opposite_corner')
        return
    if tactic_empty_corner(b):
        print('Used  tactic_empty_corner')
        return
    if tactic_empty_side(b):
        print('Used  tactic_empty_side')
        return
    print('No tactic applied: error in tactic implementations')

# Question 7

def play(human_goes_first, estonto):
    print('Board is numbered\n012\n345\n678')
    board = emptyboard. copy()
    if human_goes_first:
        print('You go first...')
        print_board(board)
    else:
        print('\nComputer goes first...')
    while not (full(board) or wins('X', board) or wins('0', board)):
        if human_goes_first:
            human_move(pl, board)
        else:
            if (estonto):
                random_play(pl2, board)
            else:
                computer_move(board)
        human_goes_first = not human_goes_first
        print_board(board)
    print('\nGame over. Result:')
    if wins('0', board):
        print('You win!')
    elif wins('X', board):
        print('Computer wins!')
    else:
        print('Draw!')

# Question 9
def swap_player(p):
    if p == 'X': return '0'
    else: return 'X'

def next_boards(b, pl):
    if wins('0', b) or wins('X', b) or full(b):
        return (b, [])
    bs = []
    for i, e in enumerate(b):
        if e == '_':
            new_board = b.copy()
            new_board[i] = pl
            bs.append(new_board)
    return (b, [next_boards(x, swap_player(pl)) for x in bs])

def game_tree(pl):
    return next_boards(emptyboard, pl)

x_game_tree = game_tree('X')

def sum_x_wins(t):
    b, bs =t
    ns = wins('X', b)
    for board in bs:
        ns += sum_x_wins(board)
    return ns

x_wins = sum_x_wins(x_game_tree)

def sum_o_wins(t):
    b, bs =t
    ns = wins('0', b)
    for board in bs:
        ns += sum_o_wins(board)
    return ns

o_wins = sum_o_wins(x_game_tree)

def drawn_games (t):
    b, bs =t
    ns = wins('X', b) and not wins('0', b) and full (b)
    for board in bs:
        ns += drawn_games (board)
    return ns

drawn = drawn_games(x_game_tree)

def num_games(t):
    b, bs =t
    ns = wins('0', b) or wins('X', b) or full(b)
    for board in bs:
        ns += num_games(board)
    return ns

games = num_games(x_game_tree)


# Question 10
def sum_game_tree(f, t):
    b, bs = t
    ns = f(b)
    for sb in bs:
        ns += sum_game_tree(f, sb)
    return ns


def f(b): return wins('X', b)
xwins = sum_game_tree(f, x_game_tree)

def f(b): return wins('0', b)
o_wins = sum_game_tree(f, x_game_tree)

def f(b): return not wins('X', b) and not wins('0', b) and full (b)
draw = sum_game_tree(f, x_game_tree)

def f(b): return wins('X', b) or wins('0', b) or full(b)
games = sum_game_tree(f, x_game_tree)


# Question 11

def decode_morse(code):
    t = tree
    for c in code:
        if c == ' ':
            pass
        elif c == '.':
            n, l, r = t
            t = l
        else:
            n, l, r =t
            t= r
    if type(t) == tuple:
        n, l, r = t
        return n
    else:
        return t

def split_string(string):
    codes = []
    spaces = 0
    code = ''
    for c in string:
        if c == ' ':
            if code != '' and spaces > 0:
                codes.append(code)
                code = ''
            spaces = spaces + 1
        else:
            if spaces == 7: codes.append(' ')
            spaces = 0
            code = code + c
    if code != '': codes.append(code)
    return codes

def decode_morse_string(string):
    for code in split_string(string):
        if code == ' ': print(' ', end='')
        else: print(decode_morse(code), end='')
    print('')
 


# Maquina 2
'''random_game()'''
#Maquina 1
'''random_game_1()'''

# Dos perosnas
'''
print('Board is numbered\n012\n345\n678\n')
while not (full(b) or wins('X', b) or wins('0', b)):
       print_board(b)
       print("\n--------------------")
       human_move(pl, b)
       if pl == '0': pl ='X'
       else: pl = '0'
print_board(b)
print("\n--------------------")
print('Game over. Result:')
if wins('0', b):
   print('0 wins!')
elif wins('X', b):
   print('X wins!')
else:
   print('Any!')
'''


# Maquina y persona InicioAleatorio
'''
quien = NULL
print("Random player")

first = random.randint(1,2)

if first == int(1) :
  quien == True
else:
   quien == False
play(quien)
'''

# Maquina y persona InicioEscogido
'''
quienjuega = False
estonto = False
quien = NULL
dificultad = NULL
opciones = ('1', '2')

while (quien not in opciones and dificultad not in opciones):
    quien = input('\nChoose Player PLAYER(1) or PC(2)? ')
    dificultad = input('\nChoose Machine TONTO(1) or LISTO(2)? ')

if quien == '1':
    quienjuega = True

if dificultad == '1':
    estonto = True

play(quienjuega, estonto)
'''

# Question 9, 10
print("Calculando cuantas veces gana O..", o_wins)  # ¿En cuántos casos gana O?
print("Calculando cuantas partidas acaban en empate..", draw)  # ¿Cuántas partidas terminan en empate?
print("Calculando numero total de juegos..", games)  # Question 9 In how many cases does O win? How many games end in a draw? How many possible different games are there?

# Question 11

temporal = '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-'

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
treemod = convertTuple(tree)
print(decode_morse_string(treemod))

'''
# Calculo
print("Calculando las posibilidades de ganar de 'X'...")
print(x_wins)

'''
'''
print(x_game_tree)
print(x_wins)
print(drawn)
print(games)
print(xwins)
print(o_wins)
print(draw)
print(games)
'''
