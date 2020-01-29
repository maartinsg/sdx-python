while True:
    try:
        first=raw_input("Number 1  ")
        second=raw_input("NUmber2  ")

        result = float(first)/float(second)
        print("{} / {} = {}".format(first,second,result))
        errorFlag=False
    except ZeroDivisionError:
        print("THe answer is infinity")
        errorFlag=True

    except Exception as e:
        print("Unexpected error (())".format(e.message))
        break
    finally:
        print("Always executed")

    if not errorFlag:
        print("This message only displays if no error")
print("Good bye")
