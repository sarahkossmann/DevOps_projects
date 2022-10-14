from games import *

def get_points():
    for diff in difficulty_list:
        points_won = (diff * 3) + 5
        return points_won

def add_score_to_file():
    list_of_numbers = []
    with open('scores.txt', 'a+') as f:
        f.write("\n")
        f.write("Points just won: ")
        f.write(str(get_points()))
    with open('scores.txt', 'r') as f:
        for score in f:
            if "Points just won: " in score:
                score = score.split(":")
                for numbers in score:
                    pass
                numbers = int(numbers)
                list_of_numbers.append(numbers)
                total = sum(list_of_numbers)
    with open('scores.txt', 'a+') as f:
        print(total)
        f.write("\n")
        f.write("Total score: ")
        f.write(str(total))

    f.close()

add_score_to_file()