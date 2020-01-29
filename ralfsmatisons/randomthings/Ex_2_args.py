#proceduer orient prog 2 pierm

def getSum(*args,initial=0,maximum=50):
    total = initial
    for n in args:
        total +=n
    if total > maximum:
        total = maximum
    return total
a0 = getSum(initial=10)
a3 = getSum(2,30,4, maximum=20)
a4 = getSum(10,2,13,44, maximum=100, initial=20)

print("a-: %s" % a0)
print("a-: %s" % a3)
print("a-: %s" % a4)
