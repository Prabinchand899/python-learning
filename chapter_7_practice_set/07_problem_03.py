
# Attempt problem 1 using while loop.

n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {n}:")

i=1
while i<=10:
    print(f'{n} x {i} = {n*i}\n')
    i +=1