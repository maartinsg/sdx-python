#to enter the name
name=raw_input ("what is your name: ")
print ("Hello "+name) # to print name
actions={"action 1": "read book", "action 2": "practice with sdx", "action 3": "sleep"}
print (actions)
choice=raw_input ("your choice: ")
print("i'll" + actions[str(choice)] + "later")

