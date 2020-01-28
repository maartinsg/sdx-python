import math

class figure:
    def __init__(self, name):
        self.name=name
class square(figure):
    def __init__(self, name, a):
        figure.__init__(self, name)
        self.a = a
        def area(self):
            return self.a*self.a
class circle(figure):
    def __init__(self, name, r):
        figure.__init__(self, name)
        self.r = r
    def area(self):
        return math.pi*self.r**2

s1 = square('room', 5)
s2 = circle('pool', 2)

for r in [s1, s2]:
    print("{} area : {}".format(r.name, r.area()))
