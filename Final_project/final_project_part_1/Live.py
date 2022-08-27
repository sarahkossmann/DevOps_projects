from games import *


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")


def load_game():
    print("Please choose a game to play: \n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n2. Guess Game - guess a number and see if you chose like the computer \n3. Currency Roulette - try and guess the value of a random amount of USD in CAD")
    game_chosen = int(input("Type a number between 1 and 3: "))
    # game_difficulty = int(input("Choose your level of difficulty. Type a number from 1 to 5 : "))
    if game_chosen > 3:
        print("ERROR! You must a number between 1 and 3. Please try again.")
        load_game()
    if game_chosen == 1:
        memory_game()
    elif game_chosen == 2:
        guess_game()
    elif game_chosen == 3:
        currency_roulette()