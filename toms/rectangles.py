class rectangle:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b
    def perimeter(self):
        return self.a * 2 + self.b * 2
    def area(self):
        return self.a * self.b
    def setName(self, x):
        self.name = x
        
class square(rectangle):
    def __init__(self, name, a):
        self.name = name
        self.a = a
        self.b = a
    def setName(self, x):
        self.name = x
        
r1 = rectangle ("sq1", 2, 3)
r2 = rectangle ("sq2", 6, 4)
s1 = square ("sq1", 4)
r1.setName("ABC")

for r in [r1, r2, s1]:
    print("Rectangle name: " + r.name)
    print("Rectangle perimeter: {}".format(r.perimeter()))
    print("Rectangle area: {}" .format(r.area()))
