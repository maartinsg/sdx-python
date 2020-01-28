#########################
# Gatis phyton program  #
#########################

##your_name = raw_input("What is your name? ")
##print("Hello " + your_name) 

menu = {
    'action 2':'practice with SDx',
    'action 3':'sleep',
    'action 1':'read book',
    'default':'not a valid choce'
    }

##print("Please choose your action: ")
##print(menu)
##
your_input = raw_input("Your choce? ")
##print ("I'll '" + str(menu[str(your_input)]) + "' later")
##print (format(menu[str(your_input)]))

print (menu.get(str(your_input),"not valid"))

