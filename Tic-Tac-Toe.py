# Tic-Tac-Toe

# Import dependencies
import numpy as np
import random
from time import sleep

# Create a blank playing board
def new_board():
    return(np.zero((3,3), dtype = int, subok=True))

# With np.zero board returns same as 
#  np.array([[0,0,0]
#            [0,0,0]
#            [0,0,0]])


# Search for empty spaces
def available_moves(board):
    move_list = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                move_list.append((i,j))
    return(move_list)

# Check to see if a player has won by horizonal row

# Check to see if a player has won by vertical row

# Check to see if a player has won by a diagnal row

# Check for a tie 

# Start a game 
print('end')