''' Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''


class Programmer:
    company = "Microsoft"

    def __init__(self, name , language, salary):
        self.name = name
        self.language = language
        self.salary = salary


p = Programmer("Prabin","python",1200000)
print(p.name,p.language, p.salary, p.company)



