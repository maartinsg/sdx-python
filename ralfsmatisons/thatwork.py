

#askings Jevs name
name=raw_input("What's ur name ") #python3 is cooler with just input
print("Hello" + " " + name )

#2nd part
h={"action2": "practice with SDx", "action3": "sleep", "action1":"read a book"}

print( "Please choose your action :{} ".format(h))
choice=raw_input("What do you choose  ")
if(choice == "action1"):
    print("I'll : {}".format(h[choice]) + " " +"later")
elif(choice== "action2"):
    print("I'll : {}".format(h[choice]) + " " +"later")
elif(choice == "action3"):
    print("I'll : {}".format(h[choice]) + " " +"later")
else:
    print("type correctly")




       


