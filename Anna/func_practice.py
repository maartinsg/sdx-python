'''
def getsum(*args):
    total = 0
    for n in args:
        total += n
    return total

a0 = getsum()
a1 = getsum(2, 30, 4)
a2 = getsum(10, 2, 13, 44)

print("a0: %s" % a0)
print("a1: %s" % a1)
print("a2: %s" % a2)


def getsum(initial=0, maximum=50, *args):
    total = initial
    for n in args:
        total += n
    if total > maximum:
        total = maximum
    return total

a0 = getsum(initial=10)
a1 = getsum(2, 30, 4, maximum=20)
a2 = getsum(10, 2, 13, 44, maximum=100, initial=20)

print("a0: %s" % a0)
print("a1: %s" % a1)
print("a2: %s" % a2)
'''

def myfunc(*args, **kwargs):
    for arg in args:
        print("%s" % arg)

    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

print("### call 1")
myfunc(initial=10)

print("### call 2")
myfunc(2, 30, 4, maximum=20)

print("### call 3")
myfunc(10, 2, 13, 44, maximum=100, initial=20)
