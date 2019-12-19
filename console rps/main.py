import random

import os
os.system("cls")

# rock = 1
# paper = 2
# sci = 3

def check_user_input():
    user_input = input()
    if user_input == "rock":
        return 1
    elif user_input == "paper":
        return 2
    elif user_input == "scissors":
        return 3
    elif user_input == "clear":
        os.system("cls")
    elif user_input == "quit":
        print("\n-- User quit, terminating program. --")
        exit()
    else:
        print("\n-- You done messed up the program! Terminating! --")
    
def check_rand_input():
    return random.randrange(1,3);

def compare_results(user, rand):
    print("!-- User Picked: %s --!" % user)
    print("!-- Computer Picked: %s --!" % rand)

    if (user == 1 and rand == 1) or (user == 2 and rand == 2) or (user == 3 and rand == 3):
        print("\n-- It's a tie! You're both losers --")
    
    if (user == 1 and rand == 2):
        print("\n-- User Wins! --")
    elif (user == 1 and rand == 3):
        print("\n-- Computer Wins! --")
    
    if (user == 2 and rand == 1):
        print("\n-- Computer Wins! --")
    elif (user == 2 and rand == 3):
        print("\n-- User Wins! --")

    if (user == 3 and rand == 1):
        print("\n-- Computer Wins! --")
    elif (user == 3 and rand == 2):
        print("\n-- User Wins! --")
while 1:
    print("\n-- Please enter either 'rock', 'paper', or 'scissors' (or 'quit' to quit, 'clear' to clean screen). --")
    ui = check_user_input();
    ri = check_rand_input();
    compare_results(ui, ri)