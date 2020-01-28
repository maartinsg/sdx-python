import random

secret = random.randint(1,10)
numb = int(raw_input("Write a number between 1 and 10: "))
print(secret)

while True:
    if secret > numb:
        print("Too Low :(")
        numb = int(raw_input("Guess a number between 1 and 10: "))
    elif secret < numb:
        print("Too High :(")
        numb = int(raw_input("Guess a number between 1 and 10: "))
    else:
        print("You win!")
        break
