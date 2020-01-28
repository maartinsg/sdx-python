#dictionart

h= {"Id": 12, "name": "Python"}
print("dictionary: {}".format(h))

# acess by key
print("Value of ID:{}".format(h["Id"]))

# check key

print("Has key name? {}".format(h.has_key("name")))

#adding key
h["version"]="2.7.13"

# replaces value
h["ID"] =32
print("Updated dictionary: {}".format(h))
