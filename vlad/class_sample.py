#class definition
class Rectangle:
    def __init__(self, name, a, b):
        self.__name = name
        self.a = a
        self.b = b

    def perimeter(self):
        return self.a*2+self.b*2

    def area(self):
        return self.a*self.b

    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name

    
# Instances
r1 = Rectangle('kitchen', 2,4)
r2 = Rectangle('hall', 1,3)
r1.setName("ABC")

for r in (r1, r2):
    print("{} sides: {}, {}".format(r.getName(), r.a, r.b))
    print("{} perimeter: {}".format(r.getName(), r.perimeter()))
    print("{} area: {}".format(r.getName(), r.area()))

