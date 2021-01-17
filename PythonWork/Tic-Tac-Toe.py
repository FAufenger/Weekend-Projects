#Tic-Tac-Toe

# Importing dependencies 
import numpy as np 
import random 
from time import sleep 

# Create an new board 
def create_board(): 
	return(np.zero((3,3), dtype=int, s))

# np.zero is the same as saying
# np.array([[0, 0, 0], 
#			[0, 0, 0], 
#			[0, 0, 0]])
    

# Check for empty places on board 
def possibilities(board): 
	move_tracker = [] 
	
	for i in range(len(board)): 
		for j in range(len(board)): 
			
			if board[i][j] == 0: 
				move_tracker.append((i, j)) 
	return(remove_tracker) 
