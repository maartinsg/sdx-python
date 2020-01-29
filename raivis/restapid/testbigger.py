#!/usr/bin/env python
from requests import get, post, put, delete



ret = post('http://localhost:5000/TODOS', data={'task': 'cool task'})
print("POST({}): {}".format(ret.status_code, ret.json()))


ret = put('http://localhost:5000/TODOS/todo10',
          data={'task': 'something new'}
          )
print("GET({}): {}".format(ret.status_code, ret.text))

ret = get('http://localhost:5000/TODOS')
print("GET({}): {}".format(ret.status_code, ret.text))


print("PUT({}): {}".format(ret.status_code, ret.text))
ret = delete('http://localhost:5000/TODOS/todo10')
print("DELETE({}): {}".format(ret.status_code, ret.text))


ret = get('http://localhost:5000/TODOS')
print("GET({}): {}".format(ret.status_code, ret.text))


ret = put('http://localhost:5000/TODOS/todo10',
          data={'task': 'something new'}
          )
print("GET({}): {}".format(ret.status_code, ret.text))
