'''Write a program to print multiplication table of n using for loops in reversed
order.'''

n = int(input("Enter a number to print its multiplication table in reversed order: "))
print("multiplication table of given number in reversed order is:")

for i in range(10,0,-1):
    print(n*i)