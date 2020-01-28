while True:
    try:
        first = raw_input("number 1: ")
        second = raw_input("number 2: ")

        result = float(first) / float(second)
        print("{} / {} = {}".format(first, second, result))
        errorFlag = False

    except ZeroDivisionError:
        print("the answer in infinity")
        errorFlag = True

    except Exception as e:
        print("unexpected error ({})".format(e.message))
        break

    finally:
        print("always executed")

    if not errorFlag:
        print("you dont have any errors")


print("Good buy")
