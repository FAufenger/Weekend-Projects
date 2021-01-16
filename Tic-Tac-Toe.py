# Tic-Tac-Toe

# Import dependencies
import numpy as np
import random
from time import sleep

# Create a blank playing board
def new_board():
    return(np.array([[0,0,0],
                     [0,0,0],
                     [o,0,0]]))

# Search for empty spaces
def available_moves(board):
    1 = []

    for x in range(len(board)):
        for o in range(len(board)):
            if board[x][o] == 0:
                1.append((x,o))
    return(1)

