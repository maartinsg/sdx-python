import random
usernum = 0
realnum = random.randint(1,10)
while True:
    usernum = int(raw_input("Guess a number between 1 and 10: "))
    if int(usernum) < realnum:
        print("Too small! :(")
    elif int(usernum) > realnum:
        print("Too big! :(")
        
    else:
        print("You win! :)")
        break


