import datetime
import requests

print(datetime.datetime.now().strftime("%d-%m-%y"))

response = requests.get("https://github.com")
if response.status_code == 200:
    print("Github is up and running")

content = open("names.txt", "r")
content.write("moshe")
content.close()
for name in content.readlines():
    print(name, end='')

def save_name(name):
    name_file = open("names.txt", "a")
    name_file.write("\n")
    name_file.write(name)
    name_file.close()


def read_names():
    names = open("names.txt").readlines()
    for name in names:
        print(name, end='')


save_name("sarah1")
save_name("shalom2")
read_names()

def save_names(name, file):
    try:
        name_file = open(file, "r")
        name_file.write("\n")
        name_file.write(name)
        name_file.close()
    except FileNotFoundError:
        print("File not found")


save_names("xxx", "names123.txt")