from random import randint, randrange
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates
from datetime import date, time
#1. Create two variables name X and Y
# a. Print “BIG” if X is bigger than Y
# b. Print “small” if X is smaller than Y

first_number = str(input("Enter your first number: "))
second_number = str(input("Enter your second number: "))


def check_number(number_a, number_b):
    if not number_a.isnumeric():
        print(f"ERROR! please enter number, {number_a} is not a number")
    if not number_b.isnumeric():
        print(f"ERROR! please enter number, {number_b} is not a number")
    elif number_a > number_b:
        print("BIG")
    elif number_a < number_b:
        print("small")


check_number(first_number, second_number)

# 2. Run a “for” loop 5 times.
# a. Print iteration number every time.

for i in range(1, 6):
    print(i)
    i = i-1

# 3. If else vars:
# a. Create a variable and initialize it with a number 1-4.
# b. Create 4 conditions (if-elif) which will check the variable.
# c. print the season name accordingly:
# i. 1 = summer
# ii. 2 = winter
# iii. 3 = fall
# iv. 4 = spring

season_number = randrange(1, 5)

def check_which_season(season_chosen):
    if season_chosen == 1:
        print("summer")
    elif season_chosen == 2:
        print("winter")
    elif season_chosen == 3:
        print("fall")
    elif season_chosen == 4:
        print("spring")

check_which_season(season_number)

# 4. While loop:
# a. how many times will the following loop run?
# 10 times
# b. what will be printed last?
# 10

# 5. Write a program with variables holding the following
# a. Your age.
# b. First letter of your last name.
# c. Current shekels-dollar currency.
# d. Did you fly abroad (true/false)?
# e. Your apartment numbers.
# f. Print all variables.
# g. Add the currency to your age and check the result.

# NOTE FOR DORON: I chose euro here because the library had was not able to provide the rate for shekels, otherwise it would have been this:
# current_nis_usd_currency = CurrencyRates().get_rate(base_cur="USD", dest_cur="ILS", date_obj=today)
today = date.today()
age = 28
first_letter_of_last_name = "k"
current_eur_usd_currency = CurrencyRates().get_rate(base_cur="USD", dest_cur="EUR", date_obj=today)
flew_abroad = False
apt_number = 8
print(age,first_letter_of_last_name, current_eur_usd_currency, flew_abroad, apt_number)
print(age + current_eur_usd_currency)

# 6. Create a program which uses input with the following
# a. Ask user for his phone number
# b. Print the words “phone number” and the phone number the user entered.

user_phone_number = input("What is your phone number?")
print(f"Phone number: {user_phone_number}")

# 7. Write a program with the following
# a. Method named print_hello() that prints the word “hello”.
# b. Method named calculate() which adds 5+3.2 and prints the result.

def print_hello():
    print("hello")

def calculate(number_a=5, number_b=3.2):
    print(number_a+number_b)

print_hello()
calculate()

# 8. Write a program with the following
# a. Method that receives your name and prints it.
# b. Method that receives a number, divide it by 2, and prints the result.

def my_name():
    user_name = input("What is your name? ")
    print(user_name)

def divide_number():
    user_number = int(input("Give me a number: "))
    user_number_divided = user_number/2
    print(user_number_divided)

my_name()
divide_number()

# 9. Write a program with the following:
# a. Method that receives two numbers, add them, and return the sum.
# b. Method that receives two Strings, add space between them, and return one
# spaced string.

def sum_of_2_numbers():
    number_a = int(input("Type your first number: "))
    number_b = int(input("Type your second number: "))
    temp_list = []
    temp_list.append(number_a)
    temp_list.append(number_b)
    list_to_tuple = tuple(temp_list)
    return sum(list_to_tuple)

def spaced_string():
    first_string = str(input("enter a first word: "))
    second_string = str(input("enter a second word: "))
    return f"{first_string} {second_string}"

sum_of_2_numbers()
spaced_string()

# 10.Create a nested for loop (loop inside another loop) to create a pyramid shape

for i in range(6):
    for j in range(i):
        print("#", end=" ")
    print("")
