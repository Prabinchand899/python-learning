# Write a python program using function to convert Celsius to Fahrenheit.

def temp_converter(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in celsius: "))
print(f"Tempearature in fahrenheit is {temp_converter(c)} F")
    
