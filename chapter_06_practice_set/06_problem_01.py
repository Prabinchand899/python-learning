
# Write a program to find the greatest of four numbers entered by the user

print("enter four numbers to compare:\n ")

a = float(input())
b = float(input())
c = float(input())
d = float(input())


if (a>b) and (a>c) and (a>d):
    print(f"the greatest is {a}")
elif (b>c) and (b>d):
    print(f"the greatest is {b}")
elif(c>d):
    print(f"the greatest is {c}")
else:
    print(f"the greatest is {d}")
