while True:
    try:
        first = raw_input("Number 1: ")
        second = raw_input("Number 2: ")
        result = float(first) / float(second)
        print("{} / {} = {}".format(first, second, result))
        errorFlag = False
        
    except ZeroDivisionError:
        print("Can't divide with 0")
        errorFlag = True

    except Exception as e:
        print("Unexpected error ({})".format(e.message))
        break

    finally:
        print("Allways executed")

    if not errorFlag:
        print("No errors")
              
print("Bye")
