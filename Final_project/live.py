from games.currency_roulette import currency_roulette
from games.memory_game import memory_game
from games.guess_game import guess_game
from scores import add_score_to_file


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")


def load_game():
    while True:
        print(
            "Please choose a game to play: \n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n2. Guess Game - guess a number and see if you chose like the computer \n3. Currency Roulette - try and guess the value of a random amount of USD in CAD")
        try:
            game_chosen = int(input("Type a number between 1 and 3: "))
        except ValueError:
            print("ERROR! Not an integer! Try again.")
            continue
        if game_chosen > 3:
            print("ERROR! You must a number between 1 and 3. Please try again.")
            continue
        if game_chosen == 1:
            memory_game()
            add_score_to_file()
            return
        elif game_chosen == 2:
            guess_game()
            add_score_to_file()
            return
        elif game_chosen == 3:
            currency_roulette()
            add_score_to_file()
            return

