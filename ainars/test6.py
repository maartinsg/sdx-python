def myFunc(*args, **kwargs):
    for arg in args:
        print("%s" % arg)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


print('### call 1')
myFunc(initial=10)

print('### call 2')
myFunc(2, 30, 4, maximum=20)

print('### call 3')
myFunc(10, 2, 13, 44, maximum=100, inital=20)