#This is python cheat sheet
#Code that prints info about python
print('Python is a programming language\nthat lets you work quickly\nand integrate systems more effectively.)

#Variables and operations

r = [1, 2.0, 3, "word"]
print("list: {}".format(r))

print("4th element: {}".format(r[3]))

print("last element: {}".format(r[-1]))

a = list()

print("Variable a = {}".format(a))

#Tuple

t = (1, 3, 2)
#offset 0 (zero)
print("access by index: {}".format(t[1]))

#tupple assignment (unpacking)
(a, b, c) = t
print("unpacked a: {}".format(a))
print("unpacked b: {}".format(b))

#swap values
a, b = b, a
print("a={}; b={}".format(a,b))

#dictionary
h = {'id': 12, 'name': 'Python'}
print("Dictionary: {}".format(h))

#access by key
print("Value of 'id': {}".format(h['id']))

#check key [h.get('key',<default>)]
print("Has key 'name'?: []".format(h.has_key('name')))

#adding a key/value
h['version'] = '2.7.15'
#replace the value
h['id'] = 32
print("Updated dictionary: {}".format(h))

