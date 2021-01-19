# Cand Shop, here you can buy candies
# Maxium purchases allowed today is 5


# The list of candies to print to the screen
candy_list = [
    "Snickers",
    "Kit Kat",
    "Sour Patch Kids",
    "Swedish Fish",
    "Skittles",
    "Hershey Bar",
    "Starbursts",
    "M&Ms",
    "Heath Bar"
    ]


# The list used to store all of the candies selected inside of
candy_cart = []



# Set answer to "yes" for while loop
# Set item_list to 0 to count up to max purchase
answer = "y"
max_purchase = 5
item_list = 1


while answer == "y":
    
    # Print all of the candies to the screen and their index in brackets
    # Putting it here makes it visible after each choice is made and
    # the owner is able to change candy list and will still have a valid choices
    for i in range(len(candy_list)):
        print("[" + str(i) + "] " + candy_list[i])

    # Ask which candy the user would like to bring ho
    print("Which candy would you like to bring home?")
    selected = input("Input the number of the candy you want: ")

    # Add the candy at the index chosen to the candy_cart list
    candy_cart.append(candy_list[int(selected)])

    # Add one to allowance count
    item_list += 1
    if item_list > max_purchase:
        print('-----------------------------------------')
        print('Max purchase has been reached.')
        print('Too much candy is bad for you')
        print('If desired, please return to place a new order.')
        break    
    # ask the user if they want more candy 
    # any variable other than 'yes' will exit request)
    answer = input("Would you like to make another selection? ('(y)es' or '(n)o') ")


# Loop through the candy_cart to say what candies were brought home
print('-----------------------------------')
print(f'I brought home with me {item_list - 1} candies:')
for candy in candy_cart:
    print(candy)
