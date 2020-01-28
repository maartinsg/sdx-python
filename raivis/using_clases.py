# class definiton
class Rectangle:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2+self.b*2
    def area(self):
        return self.a*self.b
#instances
r1 = Rectangle('kitchen', 2,4)
r2 = Rectangle('hall', 1,3)

for r in [r1, r2]:
    print("{} sides: {}, {}".format(r.name, r.a, r.b))
    print("{} perimeter: {}".format(r.name, r.perimeter()))
    print("{} area: {}".format(r.name, r.area()))

