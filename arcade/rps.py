# Rock ,Paper , Scissor Game 

import random
import sys

def rps():

    game_count = 0
    player_wins = 0
    python_wins = 0
    draw_match = 0

    def rps_game():

        print("\nEnter .... \n1 for Rock \n2 for Paper \n3 for scissor \n")

        # Player Choice and Value
        player_choice = input("Enter your Choice : ")
        player_value = int(player_choice)

        if player_choice not in ['1','2','3'] :
            return rps_game()

        # Python Choice and Value
        python_choice = random.choice("123")
        python_value = int(python_choice)

        print(f"\n You choose : {str(player_value)}")
        print(f"\n Python choose : {str(python_value)} \n")

        # Game Playing rules

        def decide_winner(player_value,python_value):

            nonlocal player_wins
            nonlocal python_wins
            nonlocal draw_match

            if player_value == python_value :
                draw_match += 1
                return "Draw Match"
            
            elif player_value == 1 and python_value == 3 :
                player_wins += 1
                return "Player Wins"
            
            elif player_value == 2 and python_value == 1 :
                player_wins += 1
                return "Player Wins"

            elif player_value == 3 and python_value == 2 :
                player_wins += 1
                return "Player Wins"

            else :
                python_wins += 1
                return "Python Wins"

        game_result = decide_winner(player_value,python_value)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game count : {str(game_count)}")
        print(f"\n Player Win : {str(player_wins)}")
        print(f"\n Python Win : {str(python_wins)}")
        print(f"\n Draw Match : {str(draw_match)}")


        while True :

            print("\nPlay again ? \n Enter q for Play again or \n q for Quit the Game : ")

            play_again = input("\ny/q : ")

            if play_again.lower() not in ['y','q'] :
                continue
            else :
                break
        
        if play_again.lower() == "y" :
            return rps_game()
        
        else :
            if __name__ == "__main__" :
                sys.exit("\n Bye from RPS !\n")
            else :
                return
        
    return rps_game

play = rps()

if __name__ == "__main__" :
    play()