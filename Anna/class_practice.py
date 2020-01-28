# class definition
class Rectangle:
    def __init__(self, name, a, b):
        self.__name = name
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2+self.b*2

    def area(self):
        return self.a*self.b

    def getname(self):
        return self.__name

    def setName(self, arg):
        self.__name = arg

        
class Square(Rectangle):
    def __init__(self, name, a):
        Rectangle.__init__(self, name, a, a)

r1 = Rectangle("kitchen", 2, 4)
r2 = Rectangle("hall", 1, 3)
s1 = Square('room', 5)
s2 = Square('bath', 2)

r1.setName("room")

for r in [r1, r2, s1, s2]:
    print("{} sides: {}, {}".format(r.getname(), r.a, r.b))
    print("{} area: {}".format(r.getname(), r.area()))
    print("{} perimeter: {}".format(r.getname(), r.perimeter()))
