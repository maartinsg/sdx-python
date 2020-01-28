# testing list merging
def sumFunct(*args):
    result = 0
    y = 0
    try:
        for x in args:
            y = [y, x]
        print(y)
    except:
        print("error 1")
    try:
        for a in y:
            result += a
    except:
        print("error 2")
        return
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(sumFunct(list1, list2, list3))

