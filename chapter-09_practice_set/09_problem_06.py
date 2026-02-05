'''Write a program to mine a log file and find out whether it contains ‘python’'''


with open("log.txt", "r") as f:
    data= f.read()
    word = "python"
    if word in data.lower():
        print("The log file contains python.")
    else:
        print("The log file doesn't contains python")