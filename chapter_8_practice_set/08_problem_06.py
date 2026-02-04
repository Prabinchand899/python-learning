# Write a python function which converts inches to cms.



def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("enter lenght in inch: "))
print(f"length in centimeter is {inch_to_cm(inch)} cm")

