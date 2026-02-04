
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


sub1 = float(input("enter percentage of subject 1: "))
sub2 = float(input("enter percentage of subject 2: "))
sub3 = float(input("enter percentage of subject 3: "))

t = (sub1 + sub2 + sub3)/3
if(t>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you have passed")
else:
    print("you have failed")


