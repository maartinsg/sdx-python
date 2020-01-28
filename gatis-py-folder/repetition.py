### working with def

##def getSum(*args):
##    total = 0
##    for n in args:
##        total += n
##    return total
##
##a0 = getSum()
##a3 = getSum(2, 30, 4)
##
####print ("a3: %s" % a3)
##print (getSum(1,2,3))


##def getSum2(initial=0, mx=50, *args):
##    total = initial
##    for n in args:
##        total += n
##    if total > mx:
##        total = mx
##    return total
##
##print (getSum2(initial=10))
##print (getSum2(initial=0, mx=50, 2,3,4))


def MyFunc(*args, **kwargs):
    for arg in args:
        print ("%s" % arg)

    for key, value in kwargs.items():
        print ("%s == %s" %(key,value))

print ("### call 1")
MyFunc(initial=20)

print ("### call 2")
MyFunc(2, 30, 4, maximum=20)

print ("### call 3")
MyFunc(2, 30, 4, maximum=100, initial=20)

