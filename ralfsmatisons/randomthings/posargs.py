#proceduer orient prog
def getSum(*args):
    total = 0;
    for n in args:
        total +=n
    return total
a0 = getSum()
a3 = getSum(2,30,4)
a4 = getSum(10,2,13,44)

print("a-: %s" % a0)
print("a-: %s" % a3)
print("a-: %s" % a4)
