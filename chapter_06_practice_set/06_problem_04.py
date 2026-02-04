#  Write a program to find whether a given username contains less than 10
# characters or not.

name = input("Enter the username:  ")

if (len(name)<10):
    print("Username contains less than 10 characters")
else:
    print("Username does not contain less than 10 characters")