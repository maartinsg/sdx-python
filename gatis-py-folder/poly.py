# class definitions
import math

class Figure:
    def __init__(self, name):
        self.__name = name

class Square(Figure):
    def __init__(self, name, a):
        Figure.__init__(self, name)
        self.a = a

    def area(self):
        return self.a * self.a

class Square(Figure):
    def __init__(self, name, a):
        Figure.__init__(self, name)
        self.a = a

    def area(self):
        return self.a * self.a

r1 = Rectangle('kitchen', 2, 4)
r2 = Rectangle('hall', 1, 3)
r1 = r1.setName("ABC")

for r in [r1, r2]:
    print("{} sides: {}, {}".format(r.getName(), r.a, r.b))
    print("{} perimeters: {}".format(r.getName(), r.perimeter()))
    print("{} area: {}".format(r.getName(), r.area()))


