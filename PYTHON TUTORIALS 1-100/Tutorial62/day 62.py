"""class Employee:
    def __init__(self):
        self.__name = "Licaa"

    
a = Employee()
# print(a.name) # Cannot be accessed directly

print(a._Employee__name) 

print(a.__dir__())
"""

class Parent:
    def __init__(self):
        self.parent_variable = 100

    def protected_method(self):
        print("This is a protected method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_variable = 200

    def another_protected_method(self):
        super().protected_method()

obj = Child()
obj.protected_method()  # This is a protected method
obj.another_protected_method()  # This is a protected method