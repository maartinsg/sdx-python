name=raw_input("What is your name?")
print("Hello " + name)
dicti = {'action 2': 'practice with SDx', 'action 3': 'sleep', 'action 1': 'read book'}
print("Please choose your action: {}".format(dicti))
input=raw_input("Your choice? ")
if (input.lower()==str('action 2')):
   print("I'll " + str(dicti.get('action 2')) + " later")
elif (input.lower()==str('action 1')):
   print("I'll " + str(dicti.get('action 1')) + " later")
elif (input.lower()==str('action 3')):
   print("I'll " + str(dicti.get('action 3')) + " later")
else:
   print("Sorry, wrong input!")


