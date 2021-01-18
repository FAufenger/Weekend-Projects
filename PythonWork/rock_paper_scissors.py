# Rock Paper Scissors 1 Player vs Computer
# Shows games played and percentage of win/loss/tie

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
count_total = 0

# Before beginning, choose how many games you want to play
games_desired = int(input ("How many games would you like to play? "))
print('---------------------')

# Add while statement to see if player wants to continue
while count_total < games_desired :

    # Computer Selection (Random)
    computer_choice = random.choice(options)

    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Run Conditionals
    if (user_choice == "r" and computer_choice == "p"):
        print("You chose rock. The computer chose paper.")
        print("Sorry. You lose.")
        count_loss += 1
        count_total += 1

    elif (user_choice == "r" and computer_choice == "s"):
        print("You chose rock. The computer chose scissors.")
        print("Yay! You won.")
        count_win += 1
        count_total += 1

    elif (user_choice == "r" and computer_choice == "r"):
        print("You chose rock. The computer chose rock.")
        print("Oh dear, a tie!")
        count_tie += 1
        count_total += 1

    elif (user_choice == "p" and computer_choice == "p"):
        print("You chose paper. The computer chose paper.")
        print("Oh dear, a tie!")
        count_tie += 1
        count_total += 1

    elif (user_choice == "p" and computer_choice == "s"):
        print("You chose paper. The computer chose scissors.")
        print("Sorry. You lose.")
        count_loss += 1
        count_total += 1

    elif (user_choice == "p" and computer_choice == "r"):
        print("You chose paper. The computer chose rock.")
        print("Yay! You won.")
        count_win += 1
        count_total += 1

    elif (user_choice == "s" and computer_choice == "p"):
        print("You chose scissors. The computer chose paper.")
        print("Yay! You won.")
        count_win += 1
        count_total += 1

    elif (user_choice == "s" and computer_choice == "s"):
        print("You chose scissors. The computer chose scissors.")
        print("Oh dear, a tie!")
        count_tie += 1    
        count_total += 1

    elif (user_choice == "s" and computer_choice == "r"):
        print("You chose scissors. The computer chose rock.")
        print("Sorry. You lose.")
        count_loss += 1
        count_total +=1

    else:
        print("I don't know that choice!")
        print("Next time, choose from 'r', 'p', or 's'.")
    

percent_win = round(((count_win / count_total) * 100), 2)
percent_loss = round(((count_loss / count_total) * 100), 2)
percent_tie = round(((count_tie / count_total) * 100), 2)

# Count wins, losses and ties
print('---------------------')
print(f'Thanks for playing {count_total} games!')
print(f'You won {count_win} games, {percent_win}%')
print(f'You lost {count_loss} games, {percent_loss}%')
print(f'You tied {count_tie} games, {percent_tie}%')