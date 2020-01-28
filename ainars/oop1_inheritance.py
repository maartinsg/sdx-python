#class definiton
class Rectangle:
    def __init__(self, name, a, b):
        self.__name = name
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2+self.b*2

    def area(self):
        return self.a*self.b

    def getName(self):
        return self.__name

#makes option to change name with self.setName()
    def setName(self, name):
        self.__name = name

#Square class uses Rectangle class
class Square(Rectangle):
    def __init__(self, name, a):
        Rectangle.__init__(self, name, a, a)


#instances
r1 = Rectangle('Kitchen', 2, 4)
r2 = Rectangle('Hall', 1, 3)
r1.setName("ABC") #optional
s1 = Square('Room', 5)
s2 = Square('Bath', 2)

for r in [r1, r2, s1, s2]:
    print("{} sides are {}m and {}m.".format(r.getName(), r.a, r.b))
    print("{} perimeter is {}sqm.".format(r.getName(), r.perimeter()))
    print("{} area is {}sqm.".format(r.getName(), r.area()))
