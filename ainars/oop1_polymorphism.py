import math


# c lass definition
class Figure:
    def __init__(self, name):
        self.name = name


class Squere(Figure):
    def __init__(self, name, a):
        Figure.__init__(self, name)
        self.a = a

    def area(self):
        return self.a*self.a


class Circle(Figure):
    def __init__(self, name, r):
        Figure.__init__(self, name)
        self.r = r

    def area(self):
        return math.pi*self.r**2


# instances
s1 = Squere('room', 5)
c1 = Circle('pool', 2)

for r in [s1, c1]:
    print('{} area: {:.2f}'.format(r.name, r.area()))