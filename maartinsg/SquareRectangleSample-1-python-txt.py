import math

class Figure:
    def __init__(self, name):
        self.name = name

class Square(Rectangle):
    def __init__(self, name, a):
        Figure.__init__(self, name)
        self.a = a

class Circle:
    def __init__(self, name, r)
        Figure.__init__(self,name)
        self.r = r

    def area(self):
        return math.pi*self.r**2

# Instanced?
#r1 = Rectangle('Kitchen', 2, 4)
#r2 = Rectangle('Hall?', 1, 3)
s1 = Square('room', 5)
r4 = Circle('pool', 2)

for r in [r1, r2, s1, s2]:
    print("{} sides: {}, {}".format(r.name, r.a, r.b))
    print("{} perimeter: {}, {}".format(r.name, r.a, r.b))
    print("{} sides: {}, {}".format(r.name, r.a, r.b))
