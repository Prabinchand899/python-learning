#  Write a program which finds out whether a given name is present in a list or not

names = ['alice', 'bob', 'charlie', 'david', 'eve']
n = input("Enter the name to search: ").lower()

if n in names:
    print(f"{n} is present in the list.")
else:
    print(f"{n} is not present in the list.")