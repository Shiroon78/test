class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.raius = radius
        super().__init__(radius, radius)
    def area(self):
        return super().area() * 3.14

c = Circle(5)
print(c.area())