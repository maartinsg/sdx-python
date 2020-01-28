nameInput = raw_input("What is your name? ")
print("Hello " + nameInput)
print("Please choose your action:")
d1 = { 'action 2': 'practice with SDx','action 3': 'sleep', 'action 1':'read book'}
print("{}".format(d1))
choiceInput = raw_input("Your choice:")
if (d1.has_key(choiceInput)):
    print("I'll '{}' later".format(d1.get(choiceInput, None)) )
else:
    print("Wrong choice of action was input!")
