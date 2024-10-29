#Christopher Kenny
#CS 175
#Strings Assignment 3

name = input("Enter your name: ")
last = input("Enter your last name: ")
id = input("Enter your ID number: ")

name_1 = name[0:3]
last_1 = last[0:3]
id_1 = id[-3:]

login_name = name_1 + last_1 + id_1
print(f"Your system login name is: {login_name}")
