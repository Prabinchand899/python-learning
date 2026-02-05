'''Repeat program 4 for a list of such words to be censored.'''


words = ["Donkey","bad","shit","donkey"] 

with open("donkey.txt","r") as f:
    data = f.read()
    for word in words:
         data = data.replace(word,"#"*len(word))

with open("donkey.txt", "w") as f:
    f.write(data)

