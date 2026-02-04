
# Write a program to calculate the factorial of a given number using for loop.

num = int(input('Enter a number to find its factorial: '))
f=1

for i in range(1,num+1):
    f=f*i
    
print(f'The factorial of {num} is {f}')
