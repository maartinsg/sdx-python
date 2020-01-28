import random
secret = random.randint(1, 10)
inputNumber = None
while inputNumber != secret :
    inputNumber = int(raw_input ("Guess a number between 1 and 10: "))
    if (isinstance(inputNumber, int)):
        if (inputNumber > secret) :
            print("Too High :(")
        elif (inputNumber < secret) :
            print("Too Low :(")
        else:
            print("You Win! :)")
    else:
        print("Not a number!")
        break
