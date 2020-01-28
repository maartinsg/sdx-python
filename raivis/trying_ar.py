#def getSum(*args):
#    total = 0
#    for n in args:
#        total +=n
#    return total

#print("{0:d}".format(a0))
#print("{0:d}".format(a1))
#print("{0:d}".format(a2))

#def myFunc(*args, **kwargs):
#    for arg in args:
#        print("%s" % arg)

#    for key, value in kwargs.items():
#        print("%s == %s" % (key, value))

#print("### call 1")
#myFunc(initial=10)
#print("### call 2")
#myFunc(2, 30, 4, maximum=20)
#print("### call 3")
#myFunc(10, 2, 13, 44, maximum=100, initial=20)

while True:
    try:
        first = raw_input("Number 1: ")
        second = raw_input("Number 2: ")

        result = float(first) / float(second)
        print("{} / {} = {}".format(first, second, result))
        errorFlag = False
    except ZeroDivisionError:
        print("The answer is infinity")
        errorFlag = True

    except Exception as e:
        print("Operation error ({})".format(e.message))
        break

    finally:
        print("Always executed!")

    if not errorFlag:
        print("This message only displays if there is no error!")

print("Good boy!")
