

class Employee:
    language = "py"

    def __init__(self,name,language,salary):   #dunder method which is automatically called
        print("Creating an object")
        self.name= name
        self.language = language
        self.salary = salary


    


mingo = Employee("mingo","js",12000)
print(mingo.name,mingo.language,mingo.salary)