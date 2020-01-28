menu = {
    'action 1': 'read book',
    'action 2': 'practice with SDx',
    'action 3': 'sleep'
    }
name = raw_input("What is your name? ")
print ("Hello " + name)
print("Please choose your action:")
print(menu)
item = raw_input("Your choice? ")
print("I`ll '" + str(menu[str(item)]) + "' later")
