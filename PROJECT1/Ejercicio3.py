#!/usr/bin/python3
#coding: utf-8
import random
i = 0
b = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
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

def print_board(b):
    for n, x in enumerate(b):
        print(x, end='')
        if n % 3 == 0: print('')

def full(b):
    return '_' not in b

def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b^[x] for x in l]
        if bl == win: return True
    return False

def random_move(NumeroRandom, b):
    NumeroRandom = random.randint(0, 8)
    for x in b:
        vacio_o_no(random)
    
        
def vacio_o_no(random):
    if b[x] == '_': return random
    

#while i<1:
#    print(NumeroRandom)
    
#    print(list(range(0,100,5)))
    # ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    #Persona1=input("Persona1:")
    #Persona2=input("Persona2:")
    #full(Persona1)
    #print_board(Persona1)
    #if wins(Persona1, Persona2): 
    #    print('GANO')
#    i=i+1 










#Jugada_aleatoria(player)

#while final != true:
    #num_aleatorio(0,8)
    #check_position(num_aleatorio, empty)    
    
    #if (empty == true)
        #write_pos(numero, player)
        

    #check_won(b, won, player )   
     
    #if (won ==true)
        #final = true

