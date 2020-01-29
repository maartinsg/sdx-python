from requests import post, get, put

ret = put(
    'http://localhost:5000/todos/todo10',
    data={'task': 'somthing coool'}
    )
print("PUT({}): {}".format(ret.status_code, ret.json()))

ret = get('http://localhost:5000/todo1')
print("GET({}): {}".format(ret.status_code, ret.json()))

##ret = post('http://localhost:5000/todos', data={'task': 'cool task'})
##print("POST({}): {}".format(ret.status_code, ret.json()))

