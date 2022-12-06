from games import *
import os

def get_points():
    for diff in difficulty_list:
        if diff == 0:
            points_won = 0
        else:
            points_won = (diff * 3) + 5
        return points_won

def add_score_to_file():
    list_of_numbers = []
    with open('scores.txt', 'a+') as f:
        if os.stat("scores.txt").st_size:
            f.write("\n")
            f.write("Points just won: ")
            f.write(str(get_points()))
        else:
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
        f.write("\n")
        f.write("Total score: ")
        f.write(str(total))
    f.close()

def delete_first_two_rows():
    with open("scores.txt", 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for number, line in enumerate(lines):
            if number not in [0, 1]:
                f.write(line)
    f.close()

# add_score_to_file()
# delete_first_two_rows()