# Multo[;e inherianc
class Employee:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"the name is {self.name}")
class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}")
class Dancer_Emplyee(Dancer, Employee):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

L = Dancer_Emplyee("Lica", "Folk")
print(L.name)
print(L.dance)
print(Dancer_Emplyee.mro())
L.show()