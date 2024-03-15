class Emplyee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


e1 = Emplyee("Licaa", 120000)
print(e1.name)
print(e1.salary)

string = "Licaa-120000"
# e2 = Emplyee(string.split("-")[0], string.split("-")[1])
# print(e2.anme)
# print(e2.salary)
e2 = Emplyee.fromStr(string)
print(e2.name)
e2a = int(e2.salary)
print(e2a, type(e2a))