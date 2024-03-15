class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Person("Angel", 17)
print(a.__dict__)