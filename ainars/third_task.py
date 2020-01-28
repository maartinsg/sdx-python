import random
secret = random.randint(1, 10)
while True:
    guess = int(raw_input("Guess a number between 1 and 10: "))
    print(guess)
    if (guess) == secret:
        print("You Win! :)")
        break
    elif (guess) > secret:
        print("Too High :(")
    else:
        print("Too Low :(")
