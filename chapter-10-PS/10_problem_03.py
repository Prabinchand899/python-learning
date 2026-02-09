'''. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''


class new:
    a = 2

obj = new()
obj.a = 0
print(obj.a)
print(new.a) #class attribute not changed



