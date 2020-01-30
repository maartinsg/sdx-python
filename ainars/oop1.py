#class definiton
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
r1 = Rectangle('Kitchen', 2, 4)
r2 = Rectangle('Hall', 1, 3)

for r in [r1, r2]:
    print("{} sides are {}m and {}m.".format(r.name, r.a, r.b))
    print("{} perimeter is {}sqm.".format(r.name, r.perimeter()))
    print("{} area is {}sqm.".format(r.name, r.area()))
