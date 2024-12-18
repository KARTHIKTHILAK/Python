# Arcade Collection of my Two Games
import sys
import rps
import guess

def full_arcade():
    
    print("\nWelcome to Karthik's Arcade \n Enter 1 for play RPS game or \n 2 for Guess the number game : ")

    game_value = input("\nWhich Game : ")
    
    def enter_game(game_value):

        if game_value == "1" :
            print(rps.play())
        elif game_value == "2" :
            print(guess.guess())

    game = enter_game(game_value)

    print(game)

    while True :

        print("\nYou want to play again in Arcade : \n Enter p for play again or \n Enter x for quit from Arcade \n")
        arcade_play_again = input("p/x : ")

        if arcade_play_again not in ['p','x'] :
            continue

        else : 
            break

    if arcade_play_again == 'p' :
        print("Welcome Back ! ")
        return enter_game(game_value)
    
    elif arcade_play_again == 'x' :
        sys.exit("Bye from Arcade !")


full_arcade()    