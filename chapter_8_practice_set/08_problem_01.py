
#  Write a program using functions to find greatest of three numbers.


def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
    
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

print(f"greatest number among given is {great(a,b,c)} ")