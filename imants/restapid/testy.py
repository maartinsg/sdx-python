#!/usr/bin/env python
from requests import get, put, post, delete

#ret = post ('http://localhost:5000/todos', data={'task': 'cooltask'})
#print("POST({}): {}".format(ret.status_code, ret.json()))

#ret = put (
    #'http://localhost:5000/todos/todo10',
    #data={'task': 'something cool'}
   # )
#print("PUT({}): {}".format(ret.status_code, ret.json()))

ret = get ('http://192.168.8.105:5000/TODOS')
print("GET({}): {}".format(ret.status_code, ret.json()))

#ret = delete('http://localhost:5000/todos/todo10')
#print("DELETE({}): {}".format(
    #ret.status_code,
    #ret.text))

#ret = get ('http://localhost:5000/TODOS')
#print("GET({}): {}".format(ret.status_code, ret.json()))

#ret = put (
   # 'http://localhost:5000/todos/todo10',
   # data={'task': 'something cool'}
    #)
#print("PUT({}): {}".format(ret.status_code, ret.json()))
