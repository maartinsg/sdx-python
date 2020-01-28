person = "Luke"

if person == "Ainars":
    status = "Guy"
elif person == "Luke":
    status = "Jedi"
else:
    status = "unknown"

print("{} - {}".format(person, status))

status_map = {'Ainars': 'Guy', 'Luke': 'Jedi'}
person = "Ainars"
print("%s = %s" % (person, status_map.get(person)))


