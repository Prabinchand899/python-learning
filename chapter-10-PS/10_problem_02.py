'''Write a class “Calculator” capable of finding square, cube and square root of a
number.'''

class Calculator:

    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The squre is {self.n*self.n}")
    def cube(self):
        print(f"The squre is {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"The squre is {self.n*self.n**1/2}")
    
    

n = Calculator(3)
n.square()
n.cube()
n.sqrt()
