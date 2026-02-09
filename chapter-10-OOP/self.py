

class Employee:
    language = "py"

    def getinfo(self):      #the argument "self" should be given whether it's used or not.
        print(f"The language is {self.language}")

    @staticmethod      #this defines that the greet function doesn't require any argument.
    def greet():
        print("Good day sir!")


mingo = Employee()
mingo.greet()
mingo.getinfo()    
Employee.getinfo(mingo)   #line 11 and line 12 are same statements

# print(Employee().language)