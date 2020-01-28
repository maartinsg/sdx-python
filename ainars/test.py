#My first python app
#Hello world
print('Hello World') #' or "
print("It's good") #double with single in text = good
print('It\'s good') #if ' in text \' to escape
print("Mani sauc\nAinars") #new line
print('''Mani 
sauc
Ainars''') #new line with ''' or """ with enter
#name = raw_input("What's your name?\n")
#print('Your name is %s!' % name)
my_name = 'Ainars'
print('My name is {0:}!'.format(my_name))#may also work with {}
s = "this is my testing string"
print(s.count('is'))
print(s.find('my'))
three = '3'
print(three.isdigit())
print(s.isdigit())
uppercases = s.upper()
print(s)
print(uppercases)#converts to upper cases
s=s.upper()
print(s)#overwrites s string
new_s=s.replace('MY', 'YOUR')
print(new_s)
x_s=s.replace('T', 'X', 1)#replace only one !!
print(x_s)
print(s.rjust(30))
print(s.ljust(30))

r = [1, 2.0, 3, "5"]
print("list: {}".format(r))
#access by index
print("2nd element: {}".format(r[1])) #negative index counts from end
print("Slice: {}".format(r[1:3]))
w = r + [10, 19] #concatane list; gives another list
print("w list {}".format(w))
t = [0.0] * 5 #create an inital vector using repetition
print("t list {}".format(t))
empt=list() #makes empty list

members = ['Peteris', 'Imants', 'Janis', 'Anna']

members.sort() #updates list

print("Janis is a member? {}".format('Janis' in members))

tp = (1, 2, 3) #TUPLE!! not a list
print("access by index:".format(t[1]))

(a, b, c) = tp #tuple assignment (unpacking)
print('unpacked a: {}'.format(b))

#swap values
a, b = b, a
print("a={}, b={}".format(a,b))

#convert tuple to list
rr = list(tp)
#convert list to tuple
tp2 = tuple(rr)

#DICTIONARYYYYYYYYY

h = {'id': 12, 'name': 'Python'}
print("Dictionary: {}".format(h))
print("Value of 'id': {}".format(h['id'])) #only check if there is key, not a value
print("Value of 'id': {}".format(h.get('id',)))
print("Has hey 'name'?: {}".format(h.has_key('name')))
h['version'] = '2.7.13' #add key/value
h['id'] = 32 #replace value
print("Updated dictionary: {}".format(h))
print("Keys: {}".format(h.keys()))


