

'''Write a program to find out whether a file is identical & matches the content of
another file.
'''

with open("this.txt","r") as f:
    content1 = f.read()

with open("copy.txt","r") as f:
    content2 =f.read()

if content2 == content1 :
    print("files are identical")
else:
    print("files are not identical")
    