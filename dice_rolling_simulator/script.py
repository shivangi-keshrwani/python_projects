# Dice Rolling Simulator - Python Project

import random as rm

choice = True

while choice:
    num = rm.randint(1, 6)
    print("You got", num)
    c = input("Do you want to roll the dice again. (Y/N): ")
    if c == 'N' or c == 'n':
        choice = False
    elif c == 'Y' or c == 'y':
        choice = True
    else:
        print("Please enter a valid choice")
        choice = False
