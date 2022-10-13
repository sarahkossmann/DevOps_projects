from random import randint
from time import sleep
from forex_python.converter import CurrencyRates
from datetime import date


def memory_game():
    while True:
        difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        attempts = 3
        print("A sequence of numbers will appear for one second. Remember them.")
        sleep(2)
        sequence_of_numbers = [(randint(1, 100)) for i in range(difficulty)]

        while True:
            while attempts > 0:
                sleep(2)
                print(sequence_of_numbers, end="")
                sleep(1)
                print(" " * len(sequence_of_numbers), end="\r")
                sleep(1)

                user_answer_number = str(input("Guess the numbers you just saw (in the right order). \nProvide list of numbers separated by comma, e.g. 1,2,3. \nType the sequence here: "))
                user_answer_split = user_answer_number.split(',')

                if len(user_answer_split) != 3:
                    print('Please enter only 3 numbers')
                    continue

                flag = True
                for elem in user_answer_split:
                    if not elem.isnumeric():
                        flag = False
                        break
                if not flag:
                    print('Please enter only numbers')
                    break

                for i in range(len(sequence_of_numbers)):
                    sequence_of_numbers[i] = str(sequence_of_numbers[i])
                if sequence_of_numbers == user_answer_split:
                    print('Congrats! You won!')
                    exit()
                else:
                    attempts -= 1
                    print(f"You have {attempts} attempt(s) left.")

            if attempts == 0:
                print('Game over')
                exit()

def guess_game():
    while True:
        difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        attempts = 7 - difficulty
        computer_number = str(randint(1, 100))

        while attempts > 0:
            user_number = input("Guess the number the computer is thinking about. Choose a number between 1 and 100: ")
            if not user_number.isnumeric():
                print("Error. You should enter a numeric character")
            elif computer_number != user_number:
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
    while True:
        difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        today = date.today()
        value_number_usd = randint(1, 100)
        usd_in_cad = CurrencyRates().convert(base_cur="USD", dest_cur="CAD", amount=value_number_usd, date_obj=today)
        usd_in_cad = round(usd_in_cad, 1)
        user_guess = float(input(
            f"Here is {value_number_usd} USD. \nGuess how much this amount is in Canadian Dollars (accuracy 1 decimal after the coma): "))
        interval = 6 - difficulty
        if user_guess in range(usd_in_cad - interval, usd_in_cad + interval):
            print("You guessed right!")
        else:
            print(f"Game over. The answer was {usd_in_cad}")

currency_roulette()
