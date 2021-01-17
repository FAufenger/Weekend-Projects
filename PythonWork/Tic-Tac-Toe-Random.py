#Tic-Tac-Toe Simulator
## UNDER CONSTRUCTION!!

# Importing dependencies 
import numpy as np 
import random 
from time import sleep 
import matplotlib.pyplot

# Create an new board 
def create_board(): 
	return(np.zeros((3,3), dtype=None, order='C'))

# np.zero((3,3)) is the same as saying:
# np.array([[0, 0, 0], 
#			[0, 0, 0], 
#			[0, 0, 0]])
    

# Set create_board() equal to a variable 
board = create_board()


# Add place holder to save where player 1 moves
# Players will change the board position to their number
# Player 1=1 and Player 2=2

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

place(board, 1, (0, 0))


#----------------------------

# Check for empty places on board 
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))


# Another more round about way to do the same thing:
# def possibilities(board): 
# 	move_tracker = [] 
	
# 	for i in range(len(board)): 
# 		for j in range(len(board)): 
			
# 			if board[i][j] == 0: 
# 				move_tracker.append((i, j)) 
# 	return(move_tracker) 



# Prited to check what would print
#print(possibilities(board))

# We recieved a list of tupples for each open space
#[(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# Note (0,0) is removed since we used player one to move there first 

#-------------------------------

# Creating a move for 


print('end of program')