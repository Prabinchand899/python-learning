
def fact(n):
    if n==0 or n ==1:
        return 1
    return n * fact(n-1)

n = int(input("enter a number: "))
print(f"the factorial of given number is {fact(n)}")