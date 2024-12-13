# Rock Paper Scissor Project

import random       # Import random for Computer_choice
import sys          # Import sys for error making for Player
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("")

play_again = True

while play_again:
    
    print(" ")
    
    print("Welcome to ROCK , PAPER , SCISSOR Game : ")
    
    print(" ")
    
    Player1_choice = input("Enter....\n1 for Rock,\n2 for Paper,\n3 for Scissor :\n\n")    
    Player1_value = int(Player1_choice)
    
    if Player1_value < 1 or Player1_value > 3:
        sys.exit("You must enter 1 , 2 , 3 only.") 
        
    Computer_choice = random.choice("123") 
    Computer_value = int(Computer_choice) 
    
    print("") 
    
    print("You Choose : " + Player1_choice + " " + str(RPS(Player1_value)).replace("RPS.", " ") + ".")
    print("Python Choose : " + Computer_choice + " " + str(RPS(Computer_value)).replace("RPS.", " ") + ".")
    
    print("") 
    
    # Game Playing Rules
    
    if Player1_value == Computer_value: 
        print("Draw Match")
    elif Player1_value == 1 and Computer_value == 3: 
        print("Won by Player1") 
    elif Player1_value == 2 and Computer_value == 1: 
        print("Won by Player1")
    elif Player1_value == 3 and Computer_value == 2:
        print("Won by Player1")
    else:
        print("Won by Python") 
    
    print("")
    
    print("Play again ? \nEnter y for Play again \nEnter q for Quit ")
    
    last_value = input("y/q : ")
    
    if last_value.lower() == "y" :
        continue
    
    if last_value.lower() == "q": 
        play_again = False   
    
    else:
        print("Invalid value enter y or q correctly")
        break
    
    sys.exit("Bye")

print(" ")