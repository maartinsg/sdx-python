def getSum(initial=0, maximum=50, *args):  #=0/50 means that if u dont specifie, it will set to default 0 or 50
    total = initial
    for n in args:
        total += n
    if total > maximum:
        total = maximum
    return total


a0 = getSum(initial=10)
a3 = getSum(maximum=20, arg=(2, 30, 4))
a4 = getSum(10, 2, 13, 44, maximum=100, initial=20)

print("a0: %s" % a0)
print("a3: %s" % a3)
print("a4: %s" % a4)
