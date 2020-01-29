#!/usr/bin/env python2
# ///////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////// #

import random

# to guess the number - testing maths Python v.2 or maybe Python v.3

secret = random.randint(1, 10)

guessnumber = 0
while (guessnumber != secret):
        #it is needed to typecast to int this raw_input
        guessnumber = int(raw_input("Guess a number between 1 and 10 please: "))
        if (guessnumber < secret):
            print("Too Low :(")
        elif (guessnumber > secret):
            print("Too High :(")
        else:
            continue
print("You won earlier! :)")
