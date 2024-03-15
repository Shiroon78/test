class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal!")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"Woof! I am a {self.breed}!")

dog = Dog("Max", "Labrador")
dog.speak()
dog.bark()