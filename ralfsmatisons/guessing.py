import random
value=0
rnd=random.randint(1,10)
while(value !=rnd):
    
    value=raw_input("Enter a value between 1 and 10 ")


if (value== rnd):
    print("You have guessed the value")
elif(value > rnd):
    print("Too high")
elif(value< rnd):
    print("Too low :C ")
else:
    print("you win")

