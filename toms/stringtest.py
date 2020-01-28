#test to print some text

print('''This is a \'
text in\n\'multiple lines that has\nsome
\' characters\" \n''')

#test for lists

z = [1, 5.5, "some text", True]
print("{}".format(z))

#test for list operations
z.append("to replace")
print("{}".format(z))
z[4] = "replaced"
print("{}".format(z))

#test for tuple
x = (1, 5.5, "some text", True)
print("{}".format(x))

#test for dictionary
c = { "id":12, "name":"Python"}
print("{}".format(c))
c["name"] = "Toms"
print("{}".format(c.get("name",None)))
