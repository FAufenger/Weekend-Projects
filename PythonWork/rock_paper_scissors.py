# Rock Paper Scissors 1 Player vs Computer
## Under CONSTRUCTION
# Adding couter and while statement to ask if you want to play again


# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
# And set up conters for outcomes
options = ["r", "p", "s"]
count_win = 0
count_loss = 0
count_tie = 0
answer = 'y' 

# Computer Selection (Random)
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Add while statement 
#While answer == 'y'

# Run Conditionals
if (user_choice == "r" and computer_choice == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry. You lose.")
    count_loss += 1

elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("Yay! You won.")
    count_win += 1

elif (user_choice == "r" and computer_choice == "r"):
    print("You chose rock. The computer chose rock.")
    print("Oh dear, a tie!")
    count_tie += 1

elif (user_choice == "p" and computer_choice == "p"):
    print("You chose paper. The computer chose paper.")
    print("Oh dear, a tie!")
    count_tie += 1

elif (user_choice == "p" and computer_choice == "s"):
    print("You chose paper. The computer chose scissors.")
    print("Sorry. You lose.")
    count_loss += 1

elif (user_choice == "p" and computer_choice == "r"):
    print("You chose paper. The computer chose rock.")
    print("Yay! You won.")
    count_win += 1

elif (user_choice == "s" and computer_choice == "p"):
    print("You chose scissors. The computer chose paper.")
    print("Yay! You won.")
    count_win += 1

elif (user_choice == "s" and computer_choice == "s"):
    print("You chose scissors. The computer chose scissors.")
    print("Oh dear, a tie!")
    count_tie += 1    

elif (user_choice == "s" and computer_choice == "r"):
    print("You chose scissors. The computer chose rock.")
    print("Sorry. You lose.")
    count_loss += 1

else:
    print("I don't understand that!")
    print("Next time, choose from 'r', 'p', or 's'.")

# Count wins, losses and ties
Print(f'')