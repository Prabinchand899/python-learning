
'''Write a program to find out the line number where python is present from ques 6.'''

n=1

with open("log.txt","r") as f:
    data= f.readlines()

    for line in data:
        if("python" in line):
            print(f"Python is present in line {n}")
            break
        n = n+1
        
            
    else:
        print("Python is not present in the file")

