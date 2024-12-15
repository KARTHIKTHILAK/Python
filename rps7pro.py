# Rock Paper Scissor Project

import random       # Import random for Computer_choice
import sys          # Import sys for error making for Player
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

def rps():

    played_game_count = 0
    python_wins = 0
    player_wins = 0

    def rps_game():
        
        print("\nWelcome to ROCK , PAPER , SCISSOR Game : \n")

        # Player_1 choice and value

        Player1_choice = input("Enter....\n1 for Rock,\n2 for Paper,\n3 for Scissor :\n\n")    
        Player1_value = int(Player1_choice)

        if Player1_choice not in ["1","2","3"]:
            print("You must enter 1, 2, or 3.")
            return rps_game()
        
            
        # Python choice and value

        Computer_choice = random.choice("123") 
        Computer_value = int(Computer_choice) 

        
        print(f"\nYou Choose : {str(RPS(Player1_value)).replace("RPS.", " ")}.")
        print(f"Python Choose : {str(RPS(Computer_value)).replace("RPS.", " ")}.\n")
        
        
        # Game Playing Rules
        
        def decide_winner(Player1_value,Computer_value):

            nonlocal player_wins
            nonlocal python_wins
                
            if Player1_value == Computer_value: 
                return "😐Draw Match😐"
            
            elif Player1_value == 1 and Computer_value == 3:
                player_wins += 1 
                return "🥇Won by Player1🏆" 
            
            elif Player1_value == 2 and Computer_value == 1:
                player_wins += 1 
                return "🥇Won by Player1🏆"
            
            elif Player1_value == 3 and Computer_value == 2:
                player_wins += 1
                return "🥇Won by Player1🏆"
            
            else:
                python_wins += 1
                return "🐍Won by Python🐍" 

        game_result = decide_winner(Player1_value,Computer_value)
        print(game_result)
        
        print("")
        
        nonlocal played_game_count
        played_game_count += 1

        print(f"Game Played Count : {str(played_game_count)}")
        print(f"\nPlayer wins : {str(player_wins)}")
        print(f"\nPython wins : {str(python_wins)}")

        print(" ")
        
        print("Play again ? \nEnter y for Play again \nEnter q for Quit ")
        
        print(" ")

        while True:
            
            last_value = input("y/q : ")

            print(" ")
            
            if last_value.lower() not in ["y","q"]:
                continue          
            else:
                break

        print("")
        
        if last_value.lower() == "y" :
            return rps_game()
        
        elif last_value.lower() == "q":
            sys.exit("🙋‍♂️ Bye! 🙋‍♂️")
        
        else:
            print("Invalid value enter y or q correctly")

    return rps_game


play = rps()

play()