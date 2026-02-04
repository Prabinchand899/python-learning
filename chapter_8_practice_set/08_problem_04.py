# Write a recursive function to calculate the sum of first n natural numbers.





num = int(input("Enter a number upto which you want to calculate sum of natural numbers: "))


def sum(num):
    if num ==1:
        return 1
    else:
        return num + sum(num-1)
    

print(f" the sum of first {num} natural numbers is {sum(num)}")
