from random import randint

difficulty_list_guess_game = []

def guess_game():
    while True:
        difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        attempts = 7 - difficulty
        computer_number = str(randint(1, 100))
        print(computer_number)
        interval = 10 - difficulty

        while attempts > 0:
            user_number = input("Guess the number the computer is thinking about. Choose a number between 1 and 100: ")
            if not user_number.isnumeric():
                print("Error. You should enter a numeric character")
            computer_number = int(computer_number)
            user_number = int(user_number)
            if user_number not in range(computer_number - interval, computer_number + interval):
                print("You didn't guess the computer number.")
                attempts += -1
                print(f"You have {attempts} attempt(s) left.")
                if attempts > 0:
                    continue
                elif attempts == 0:
                    print('Game over')
                    difficulty_list_guess_game.append(0)
                    return
            else:
                print("You guessed right!")
                difficulty_list_guess_game.append(difficulty)
                return