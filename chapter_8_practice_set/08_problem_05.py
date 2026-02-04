

'''Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''


def pattern(n):

    print("*"*n)
    if n==0:
        return 
    else:
        return pattern(n-1)
    
num = int(input("enter the numberr of rows:  "))
pattern(num)