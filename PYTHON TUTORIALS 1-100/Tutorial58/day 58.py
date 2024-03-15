class Person():
    
    def __init__(self, n, o):
        print("Hey I am aperson")
        self.name = n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Rabi", "Software Engineer")
b = Person("Lica", " IT Emp")

a.info()
b.info()