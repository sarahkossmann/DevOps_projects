# 1. Write the following code: a = 1/0
# a. Build a corresponding try-except block to avoid exception

def divide(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("You can't divide by a string. Enter only Numeric")

divide(10, 0)
divide(10, "test")

# 2. Is the following code legal?
#
# try:
#     x = 1
# finally:
#     print("finally")
# Yes it is legal but it won't do anything but print "finally"

# 3. What exception types can be caught by the following handler?
# except:
# print("found an error")
# BaseException

# 4. What is wrong with using the above type of exception handler?
# The error is not specified, neither in which case the error should be thrown

# 5. What exceptions can be caught by the following handlers?
# a. except IOError
# error when trying to handle file (file not found for example)
# b. except ZeroDivisionError
# integer cannot be divided by zero

# 6. Create a text file named “words.txt” programmatically
# a. Write your name into the file

def create_write_file(file_name, name):
    file = open(file_name, "w")
    file.write(name)
    file.close()

# create_write_file("words.txt", "sarah")

# 7. Read your file content and print it
def read_file(file_name):
    file_content = open(file_name).readlines()
    print(file_content)

read_file("words.txt")

# 8. Write Hebrew content into your text file and print its content programmatically.

def write_hebrew():
    hebrew_sentence = u'שלומ'
    f = open('words.txt', 'a+')
    f.write(hebrew_sentence)
    f.close()
write_hebrew()

