# practice 1

name = raw_input("What is your name ")
print("Hello " + name)
actions = {'action 2':'practice with SDx', 'action 3':'sleep', 'action 1':'read book'}
print("Please choose your action:\n{}".format(actions))
choice = raw_input("Your choice? ")
print("I'll {} later".format(actions[choice]))
