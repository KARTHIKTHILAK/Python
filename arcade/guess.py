import random
import sys

def guess_number():

    def guess_game():

        python_guess = random.choice("123")
        python_guess_value = int(python_guess)

        print("\nPlayer guess : 1 , 2 or 3 which Python choose : ")

        player_guess = input("Enter your guess : ")
        player_guess_value = int(player_guess)

        print(f"\nPlayer Choose : {str(player_guess_value)}")
        print(f"Python Choose : {str(python_guess_value)}")

        def game_winner(player_guess_value,python_guess_value) :
            
            if player_guess_value == python_guess_value :
                return "\nPlayer Wins !"
            else : 
                return "\nPython Wins !"

        game_result = game_winner(player_guess_value,python_guess_value)
        print(game_result)

        print("\nPlay again ? \n Enter y for play again \n Enter q for quit :")

        while True :

            guess_game_again = input("\ny/q : ")

            if guess_game_again not in ['y','q'] :
                continue
            else :
                break

        if guess_game_again == 'y' :
            return guess_game()
        else :
            if __name__ == "__main__" :
                sys.exit("\nBye from Guess Number game !\n")
            else : 
                return

    return guess_game

guess = guess_number()

if __name__ == "__main__" :
    guess()