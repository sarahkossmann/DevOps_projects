from random import randint
from forex_python.converter import CurrencyRates
from datetime import date

difficulty_list_currency_roulette = []

def currency_roulette():
    while True:
        difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        today = date.today()
        value_number_usd = randint(1, 100)
        usd_in_cad = CurrencyRates().convert(base_cur="USD", dest_cur="CAD", amount=value_number_usd, date_obj=today)
        usd_in_cad = int(usd_in_cad)
        user_guess = int(input(
            f"Here is {value_number_usd} USD. \nGuess how much this amount is in Canadian Dollars: "))
        interval = 10 - difficulty
        if user_guess in range(usd_in_cad - interval, usd_in_cad + interval):
            print("You guessed right!")
            difficulty_list_currency_roulette.append(difficulty)
            return
        else:
            print(f"Game over. The answer was {usd_in_cad}")
            difficulty_list_currency_roulette.append(0)
            return