from requests import post, get

ret = get('http://localhost:5000/todo1')
print("GET({}): {}".format(ret.status_code, ret.json()))

##ret = post('http://localhost:5000/todos', data={'task': 'cool task'})
##print("POST({}): {}".format(ret.status_code, ret.json()))
