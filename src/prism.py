from math import pi, sqrt

class Prism:
    def __init__(self, shape, height):
        self.shape = shape
        self.height = height
    def surface_area(self):
        return 2 * self.shape.area() + self.shape.perimeter() * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius**2
    def perimeter(self):
        return 2 * pi * self.radius

class Square:
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width ** 2
    def perimeter(self):
        return 4 * self.width

class Triangle:
    def __init__(self, side_len):
        self.side_len = side_len
    def area(self):
        return self.side_len**2 * sqrt(3) / 4
    def perimeter(self):
        return 3 * self.side_len


c = Prism(Circle(1), 2)
print(c.surface_area())

sp = Prism(Square(2), 2)
print(sp.surface_area())

tr = Prism(Triangle(2), 2)
print(tr.surface_area())
