while True:
    try:
        first = raw_input("Number 1: ")
        second = raw_input("Number 2:")

        result = float(first) / float(second)
        print("{} / {} = {}".format(first, second, result))
        errorFlag = False
    except ZeroDivisionError:
        print("The answer is infinity")
        errorFlag = True
#        raise

    except Exception as e:
        print("Unexpected error ({})".format(e.message))
        break

    finally:
        print("Always executed!")

    if not errorFlag:
        print("This message only displays if there is no error!")
print("Good buy!")
