# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


m = int(input("Enter your marks: "))

if (m<=100 and m>90):
    print("your grade is Ex")
elif (m<=90 and m>80):
    print("your grade is A")
elif (m<=80 and m>70):
    print("your grade is B")
elif (m<=70 and m>60):
    print("your grade is C")
elif (m<=60 and m>50):
    print("your grade is D")
else:
    print("your grade is F")