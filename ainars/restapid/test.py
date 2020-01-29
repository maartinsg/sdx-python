#!/user/bin/env python
from requests import post, get, put, delete

ret = get('http://192.168.8.107:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = post('http://localhost:5000/todos', data={'task': 'cool task'})
print("POST({}): {}".format(ret.status_code, ret.json()))

ret = put('http://localhost:5000/todos/todo10', data={'task': 'something cool'})
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = delete('http://localhost:5000/todos/todo10')
print("DELETE({}): {}".format(ret.status_code,ret.text))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))




