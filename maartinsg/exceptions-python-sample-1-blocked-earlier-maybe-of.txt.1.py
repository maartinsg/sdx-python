while True:
    try:
        first = raw_input("Number 1:")
        second = raw_input("Number 2: ")

        result = float(first) / float(second)
        print("{} / {} = {}".format(first, second, result))
        errorFlag = False

    except ZeroDivisionError:
        print("The answer would be Infinity / Infinity too")
        errorFlag = True
    except Exception as e:
        print("Unexcepted or unexpected error was ({})".format(e.message))

    finally:
        print("Was always executed maybe?!")

    if not errorFlag:
        print("This message would be displayed maybe here if there would be no error or so, comprehensible.")

print("Thanks!")
