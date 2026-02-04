#  Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

s = set()
nums = [1,2,3,4,5,6,7,8]
print("enter eight numbers:")

for n in nums:
 num = int(input())
 s.add(num)

print("The unique numbers are:", s)


