import random
number=raw_input("Guess the number between 1 and 10: ")
c=random.randint (2,9)
while number != c:
    if int(number) > int(c):
        print("Too High\n")
        number=raw_input("Guess the number between 1 and 10: ")
    elif int(number) < int(c):
        print("Too low\n")
        number=raw_input("Guess the number between 1 and 10: ")
    else:
       print ("You win")
       break
