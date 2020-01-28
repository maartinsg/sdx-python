name = raw_input("What is yout name? ")
print("Hello {}".format(name))

d = {'action 1': 'read book', 'action 2': 'practice with SDx', 'action 3': 'sleep'}

while True:    
    print("Please choose your action:\n{}".format(d))
    choice = raw_input("Your choice? ")
    if choice in d.keys():        
        print("I'll {} later".format(d.get(choice)))
        break
    else:
        print("Wrong action!")
              
        

        
