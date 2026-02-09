

'''Add a static method in problem 2, to greet the user with hello.'''


class Calculator:

    def __init__(self,n):
        self.n = n
    @staticmethod
    def greet():
        print('hello user')
    
    def square(self):
        print(f"The squre is {self.n*self.n}")
    def cube(self):
        print(f"The squre is {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"The squre is {self.n*self.n**1/2}")
    
    

n = Calculator(3)
n.greet()
n.square()
n.cube()
n.sqrt()
