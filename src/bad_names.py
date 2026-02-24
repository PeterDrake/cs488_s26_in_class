import math

PI = 3.1415926535

class Circle:
    def __init__(self, x, y, radius):
        self._center = (x, y)
        self._radius = radius
    def area(self):
        return PI * self._radius * self._radius
    def circumference(self):
        return 2 * PI * self._radius
    def center(self):
        return self._center
    def overlaps(self, other):
        dx = self._center[0] - other._center[0]  # Difference in x values
        dy = self._center[1] - other._center[1]  # Difference in y values
        distance = math.sqrt(dx**2 + dy**2)
        return (self._radius + other._radius) > distance

a = Circle(3, 0, 2)
b = Circle(0, 4, 1)

print(f'Circle a is centered at {a.center()}, has an area of {a.area()}, and a circumference of {a.circumference()}')
print(f'Circle b is centered at {b.center()}, has an area of {b.area()}, and a circumference of {b.circumference()}')

print(a.overlaps(b))
