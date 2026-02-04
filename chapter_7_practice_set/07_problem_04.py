
# Write a program to find whether a given number is prime or not
num = int(input("Enter a number to check if it is prime or not: "))
s=0

for i in range(2,num):
    if num%i ==0:
        s=s+1
if s>0:
    print(f'{num} is not prime number.')  
else:
    print(f'{num} is a prime number.')      