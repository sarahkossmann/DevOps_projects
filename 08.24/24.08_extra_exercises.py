# Print First 10 natural numbers using while loop
number = 1

while number < 11:
    print(number)
    number = number + 1

# Write a program to print the following number pattern using a loop

for i in range(7):
    for j in range(1, i):
        print(j, end=" ")
    print("")

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

user_number = int(input("Enter a number: "))
sum = 0

for i in range(1, user_number+1):
    sum += i
print(sum)

# Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

