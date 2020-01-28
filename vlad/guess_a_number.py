import random

secret = random.randint(1,10)

number = 0

while True:
    
    number = raw_input("Guess a number between 1 and 10 = ")
    number = int(number)

    if number < secret:
        print("Your guess is too low.")

    if number > secret:
        print("Your guess is too high")

    if number == secret:
        print("You win!")
        break

