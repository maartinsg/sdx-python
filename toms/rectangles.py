class rectangle:
    def __init__(self, name, a, b):
        self.name = name
        self.__a = a
        self.__b = b
    def perimeter(self):
        return self.__a * 2 + self.__b * 2
    def area(self):
        return self.__a * self.__b
    def setName(self, x):
        self.name = x
        

r1 = rectangle ("1st", 2, 3)
r2 = rectangle ("2nd", 6, 4)

r1.setName("ABC")

for r in [r1, r2]:
    print("Rectangle name: " + r.name)
    print("Rectangle perimeter: {}".format(r.perimeter()))
    print("Rectangle area: {}" .format(r.area()))
