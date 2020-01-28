import random
n = random.randint(1, 10)
guess = int(raw_input("Guess a number between 1 and 10: "))
while n != "guess":
    print
    if guess < n:
        print "Too low! :("
        guess = int(raw_input("Guess a number between 1 and 10: "))
    elif guess > n:
        print "Too high! :("
        guess = int(raw_input("Guess a number between 1 and 10: "))
    else:
        print "You Win! :)"
        break
    print
