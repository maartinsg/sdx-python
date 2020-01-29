def getSum(initial=0, maximum=50, *args):  # if u don't specify, it will set to default 0 or 50
    total = initial
    for n in args:
        total += n
    if total > maximum:
        total = maximum
    return total


a0 = getSum(initial=10)
a3 = getSum(10, 10, 10, maximum=30)
a4 = getSum(10, 2, 13, 44, maximum=100, initial=20)

print("a0: %s" % a0)
print("a3: %s" % a3)
print("a4: %s" % a4)

# looks like doesn't work on python 2.7
