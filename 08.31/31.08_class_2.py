# def divide(x, y):
#     try:
#         print(x/y)
#     except ZeroDivisionError:
#         print("Don't divide by zero")
#     except TypeError:
#         print("Please use numeric characters only!")
#     except BaseException as e:
#         print("ERROR! : ", e.args)

def divide(x, y):
    if x == 0 or y == 0:
        print("Don't divide by zero")
        return
    if type(x) != int or type(y) != int:
        print("Use numeric only")
        return
    print(x/y)

print("before divide")
divide(10, 0)
divide(10, "shalom")
print("after divide")