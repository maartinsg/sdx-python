#########################
# Gatis phyton program  #
#########################

##your_name = raw_input("What is your name? ")
##print("Hello " + your_name) 

##Please choose your action:
##{'action 2':'practice with SDx', 'action 3':'sleep', 'action 1': 'read book'}
##Your choice? action 3
##I'll 'sleep' later

menu = {
    'action 2':'practice with SDx',
    'action 3':'sleep',
    'action 1':'read book'}

print("Please choose your action: ")
print(menu)

your_input = raw_input("Your choce? ")
print ("I'll '" + str(menu[str(your_input)]) + "' later")
      
