# Variables for all the exercises

first_number = 2
second_number = 1
third_number = 3

my_list = [first_number, second_number, third_number]

user_first_number = int(input("Enter your first number: "))
user_second_number = int(input("Enter your second number: "))
user_third_number = int(input("Enter your third number: "))

# 1. Write a python program to swap two numbers using a third variable

print(first_number, second_number)
temp = first_number
first_number = second_number
second_number = temp
print(first_number, second_number)

# Other solution

def swap_list(list, position_a, position_b):
    temp = list[position_a]
    list[position_a] = list[position_b]
    list[position_b] = temp
    return list

print(my_list)
print(swap_list(my_list, 0, 2))

# 2. Write a python program to swap two numbers without using third variable

print(first_number, second_number)
first_number, second_number = second_number, first_number
print(first_number, second_number)

# 3. Write a python program to read two numbers and find the sum of their cubes
sum_of_2_numbers_cubes = user_first_number**3 + user_second_number**3
print(sum_of_2_numbers_cubes)

# 4. Write a python program to read three numbers and if any two variables are equal , print that number

if user_first_number == user_second_number:
    print(user_first_number)
elif user_first_number == user_third_number:
    print(user_first_number)
elif user_second_number == user_third_number:
    print(user_second_number)
else:
    print("All numbers are different")
# 5. Write a python program to read three numbers and find the smallest among them

if user_first_number < user_second_number and user_first_number < user_third_number:
    print("The first number is the smallest")
elif user_second_number < user_first_number and user_second_number < user_third_number:
    print("The second number is the smallest")
elif user_third_number < user_second_number and user_third_number < user_first_number:
    print("The third number is the smallest")
else:
    print("Something went wrong... ")
