

f = open("file.txt")
# data =f.readlines()                  #gives line as list
# print(data, type(data))

# line1 = f.readline()
# print(line1 , type(line1))      # gives line as a string

# line2 = f.readline()
# print(line2 )      

# line3 = f.readline()
# print(line3 )      

# line4 = f.readline()
# print(line4 )     


line = f.readline()
while (line != ""):
    print(line)
    line= f.readline()
    

f.close()