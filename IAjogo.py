from jogo_da_velha import get_board

jog = None

board = 
[0, 0, 0
 0, 0, 0
 0, 0, 0]

hor = [board[0:3], board[3:6], board[6:9]]
ver = [board[0:7:3], board[1:8:3], board[2:9:3]]
dia = [board[0:9:4], board[2:7:2]]

bor = [hor, ver, dia]

 for l in bor:
    pass