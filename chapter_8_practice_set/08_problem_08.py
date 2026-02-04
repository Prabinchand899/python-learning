
# Write a python function to print multiplication table of a given number

def multi_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

num =  int(input("Enter a number to print its multiplication table: "))
multi_table(num)