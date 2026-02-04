
# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter a number to find the sum of all natural numbers upto that numebr: "))
s=0
i=1
while i<=n:
    s = s + i
    i=i+1
print(f'the sum of first {n} natural numbers is {s} ')