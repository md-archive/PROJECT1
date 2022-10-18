# !/usr/bin/python3
# coding: utf-8
from asyncio.windows_events import NULL
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
intersecting_lines = [(h1, v1, 0), (h1, v2, 1), (h1, v3, 2), (h2, v1, 3), (h2, v2, 4), (h2, v3, 5), (h3, v1, 6), (h3, v2, 7), (h3, v3, 8), (d1, h1, 0), (d1, h2, 4), (d1, h3, 8), (d1, v1, 0), (d1, v2, 4), (d1, v3, 8), (d2, h1, 2), (d2, h2, 4), (d2, h3, 6), (d2, v1, 2), (d2, v2, 4), (d2, v3, 6), (d1, d2, 4)]
pl ='0'

def print_board(b):
    for n, x in enumerate(b):
        print(x, end='')
        if n == 2 or n == 5: 
            print('') 

def instructions():
    print('Board is numbered\n012\n345\n678\n')
    
def full(b):
    return '_' not in b


def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]
        if bl == win: return True
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
    pl ='0'
    while not (full(b) or wins('X', b) or wins('0', b)):
        print_board(b)
        print("\n--------------------") 
        random_play(pl, b)
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

# Una Maquina
def random_game_1():
    b = emptyboard.copy()
    pl ='X'
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
    for l in lines:
        bl = [b[x] for x in l]
        if bl.count('_') == 1 and bl.count(piece) == 2:
            for x in l:
                if b[x] == '_': b[x] = 'X'
            return True
    return False

def tactic_win(b):
    return win_or_block(b, 'X')

def tactic_block(b):
    return win_or_block(b, '0')


def human_move(pl, board):
    n_input = input('\nPosition 0..8? ')
    #print(pl)
    if n_input.isdigit():
        n= int(n_input)
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
        if try_to_take(b, [8]): return True
    elif b[2] == 'X':
        if try_to_take(b, [6]): return True
    elif b[6] == 'X':
        if try_to_take(b, [2]): return True
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

def play(human_goes_first):
    print('Board is numbered\n012\n345\n678\n')
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
            computer_move (board)
        human_goes_first = not human_goes_first
        print_board(board)
    print('\nGame over. Result:')
    if wins('0', board):
        print('You win!')
    elif wins('X', board):
        print('Computer wins!')
    else:
        print('Draw!')


##Maquina 2
#random_game()
##Maquina 1
#random_game_1()

## Dos perosnas
#print('Board is numbered\n012\n345\n678\n')


#while not (full(b) or wins('X', b) or wins('0', b)):
#        print_board(b)
#        print("\n--------------------") 
#        human_move(pl, b)
#        if pl == '0': pl ='X'
#        else: pl = '0'
#print_board(b)
#print("\n--------------------") 
#print('Game over. Result:')
#if wins('0', b):
#    print('0 wins!')
#elif wins('X', b):
#    print('X wins!')
#else:
#    print('Any!')

 
# Maquina persona
quien = NULL
print("Random player")

first = print(random.randint(1,2))

if first == int(1) :
   quien == True

if first == int(2):
   quien == False
play(quien)
