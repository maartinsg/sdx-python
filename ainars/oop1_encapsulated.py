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


#instances
r1 = Rectangle('Kitchen', 2, 4)
r2 = Rectangle('Hall', 1, 3)
r1.setName("ABC") #optional

for r in [r1, r2]:
    print("{} sides are {}m and {}m.".format(r.getName(), r.a, r.b))
    print("{} perimeter is {}sqm.".format(r.getName(), r.perimeter()))
    print("{} area is {}sqm.".format(r.getName(), r.area()))
