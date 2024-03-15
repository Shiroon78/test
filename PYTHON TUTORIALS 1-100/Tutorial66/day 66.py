class Emplyee:
    company_name = "Apply"       #  Class Vaiable
    number_of_empl = 0
    
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Emplyee.number_of_empl += 1
    
    def showDetails(self):
        print(f"The name of the emplyee is {self.name} and the raise ammount in {self.company_name} is {self.raise_amount}")
        print(f"The size of company is {self.number_of_empl}")

# Emplyee.showDetails(emp1)
emp1 = Emplyee("Lica")     # emp1 is Instance Variable
emp1.raise_amount = 0.3
emp1.company_name = "Apple,India"
emp1.showDetails()
emp2 = Emplyee("Shiro")
emp2.company_name= ("Google")
emp2.showDetails()
print(Emplyee.company_name)


