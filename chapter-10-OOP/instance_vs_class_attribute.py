class Employee:
    language = "py"  #class attribute
    salary = 23330

mingo = Employee()
mingo.language = "js"  #instance attribute
print(mingo.language)   #instance attribute overwrites class attribute