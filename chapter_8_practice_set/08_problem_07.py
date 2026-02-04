
'''Write a python function to remove a given word from a list ad strip it at the same
time.'''

from builtins import print
import time

l = ['  hello  ', 'world', '  python  ', 'code', '  hello  ']
print(l)


word = input("Enter the word to remove form the list: ").lower().strip()


for i in range(len(l)):
    l[i] = l[i].strip()



def rmv(lst,word):
    for i in range(len(lst)):
        if word in lst:
            lst.remove(word)           
    
    print("New list is: ")
    

    return lst



if word not in l:
    print("Word not found in the list.")
else:
    print(rmv(l,word))
    
