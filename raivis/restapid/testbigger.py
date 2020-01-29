#!/usr/bin/env python
from requests import get, post, put

ret = get('http://localhost:5000/TODOS')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = post('http://localhost:5000/TODOS', data={'task': 'cool task'})
print("POST({}): {}".format(ret.status_code, ret.json()))

ret = get('http://localhost:5000/TODOS/todo1')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = put('http://localhost:5000/TODOS/todo10',
          data={'task': 'something new'}
          )
print("PUT({}): {}".format(ret.status_code, ret.json()))
