from random import randint
from time import sleep
from forex_python.converter import CurrencyRates
from datetime import date


def memory_game():
    print("A sequence of numbers will appear for one second. Remember them.")
    sleep(3)
    sequence_of_numbers = [(randint(1, 100)) for i in range(3)]
    print(sequence_of_numbers, end="")
    sleep(1)
    print(" " * len(sequence_of_numbers), end="\r")
    sleep(1)
    user_answer_number_a = input("Guess the numbers you just saw (in the right order). \nProvide list of numbers separated by comma, e.g. 1,2,3. \nType the sequence here: ")
    user_list_of_int = list(map(float, user_answer_number_a.split(',')))

    if sequence_of_numbers == user_list_of_int:
        print("Congrats! You guessed the right sequence.")
    else:
        print("Wrong answer. Please try again")
        sleep(2)
        memory_game()

def guess_game():
    attempts = 5
    computer_number = randint(1, 100)

    while attempts > 0:
        user_number = int(input("Choose a number between 1 and 100: "))
        if computer_number != user_number:
            print("You didn't guess the computer number.")
            attempts += -1
            print(f"You have {attempts} attempt(s) left.")
            if attempts > 0:
                continue
            elif attempts == 0:
                print('Game over')
                exit()
        else:
            print("You guessed right!")
            exit()

def currency_roulette():
    today = date.today()
    value_number_usd = randint(1, 100)
    usd_in_cad = CurrencyRates().convert(base_cur="USD", dest_cur="CAD", amount=value_number_usd, date_obj=today)
    usd_in_cad = round(usd_in_cad, 1)
    user_guess = float(input(f"Here is {value_number_usd} USD. \nGuess how much this amount is in Canadian Dollars (accuracy 1 decimal after the coma): "))

    if user_guess == usd_in_cad:
        print("You guessed right!")
    else:
        print(f"Game over. The answer was {usd_in_cad}")