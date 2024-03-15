# Inheritance in python

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
    

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")


e1 = Employee("Rohan Das", 478)
e1.showDetails()
e2 = Programmer("Shinro", 678)
e2.showDetails()
e2.showLanguage()