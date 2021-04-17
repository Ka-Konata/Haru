import math
import os
from random import choice, randint
from time import sleep
from datetime import datetime

NONE    = '\033[00m'
GRAY    = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
VIOLET  = '\033[35m'
VERDAO  = '\033[36m'
WHITE   = '\033[37m'

def placar():
    return f"""{BLUE}
PLACAR 
-----------------
{GREEN}jogador: {jogador}{NONE}
{RED}computador: {computad}{NONE}
{BLUE}empate: {empates}
-----------------{NONE}"""


def clear():
    print("cleaned")
    os.system('cls')


def cor(board):
    new_board = list()

    for p, this in enumerate(board):

        if board[p] == player:
            new_board.append(YELLOW + "x" + NONE)
        elif board[p] == ia:
            new_board.append(VIOLET + "o" + NONE)
        else:
            new_board.append(str(p + 1))

    return new_board


def check(board):
    global vitoria, derrota, empate
    horizontal = [board[0:3], board[3:6], board[6:9]]
    vertical   = [board[0:7:3], board[1:8:3], board[2:9:3]]
    diagonais  = [board[0:9:4], board[2:7:2]]

    b = [horizontal, vertical, diagonais]
    v = d = e = 0
    
    for classe in b:
        for linha in classe:
            if linha[0] == linha[1] == linha[2] == 1:
                v += 1
            elif linha[0] == linha[1] == linha[2] == -1:
                d += 1
            elif not 0 in linha:
                e += 1

    if v > d:
        vitoria = True
        return True
    elif d > v:
        derrota = True
        return True
    elif e == 8:
        empate = True
        return True

    return False


def player_joga():
    global board

    while True:
        try:
            jog = int(input(f"sua jogada: ")) - 1
            if jog +1 == 0:
                exit()
            if board[jog] == 0: 
                last_mov   = 1
                board[jog] = 1
                break
            elif board[jog] != 0:
                display()
                print(f"{RED}Posição ja ocupada.{NONE}")
        except (ValueError, IndexError):
            display()
            print(f"{RED}O numero das posições podem ser encontradas no tabuleiro.{NONE}")



def IA_joga():
    global board
    
    clear()
    print("a IA está jogando", end="")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print(".")
    sleep(0.3)
    print(".")
    sleep(0.3)
    display()

    while True:
        pos = randint(0, 8)
        if board[pos] == 0:
            board[pos] = -1
            break


def display():
    global board
    clear()

    new_board = list()
    for p in board:
        if p == 1:
            new_board.append("x")
        elif p == -1:
            new_board.append("o")
        else:
            new_board.append(str(p))

    print("%s | %s | %s" % (tuple(cor(new_board)[0:3])))
    print("%s | %s | %s" % (tuple(cor(new_board)[3:6])))
    print("%s | %s | %s" % (tuple(cor(new_board)[6:9])))
    print()

    """if last_mov != 0 and vez == 1:
        print(f"{YELLOW}Você jogou: {last_mov}{NONE}")
    if last_mov != 0 and vez == 2:
        print(f"{RED}Você jogou: {last_mov}{NONE}")"""


vazio    = 0
last_mov = 0
jogador  = 0
computad = 0
empates  = 0
player   = "x"
ia       = "o"

vitoria = False
derrota = False
empate  = False

vez = choice((1, -1))

board = list([vazio] * 9)
board = [1, -1, 1, 0, -1, 0, 0, -1, 0]
#board = [1, 2, 3, 4, 5, 6, 7, 8, 0]

while True:
    print(board)
    display()
    checked = check(board)
    
    if not checked:
        if vez == 1:
            player_joga()
            vez = -1

        elif vez == -1:
            IA_joga()
            vez = 1

    else:
        if empate:
            empates += 1
            print(f"{WHITE}deu empate :O{NONE}")
            print(placar())
            

        elif vitoria:
            jogador += 1
            print(f"{GREEN}parabéns! você VENCEU!{NONE}")
            print(placar())
            

        elif derrota:
            computad += 1
            print(f"{RED}você perdeu!{NONE}")
            print(placar())
        
        res = str(input("Deseja jogar novamente? [S/N] ")).lower()[0]
        if not res in "s":
            break
        board = list([vazio] * 9)
