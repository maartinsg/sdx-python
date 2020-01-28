#py 1st scrpt

name = raw_input("Enter your name : ")

print(name)

print("Hello {}".format(name))

actions = { 
        'action 1': 'read book',
        'action 2':'practice with SDx',
        'action 3':'sleep
            '}
print("Please choose your action: {}".format(actions))

choice = raw_input("your choice? ")

print("I'll %s" % str(actions.get(choice)) + " today")

#def actions_check(choice):

#    while choice != "action 1" and choice != "action 2" and choice != "action 3":

#        print("I'll %s" % str(actions.get(choice)) + " today")
