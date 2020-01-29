#!/usr/bin/env python
from requests import get, put, post, delete

ret = put (
    'http://localhost:5000/todos/todo10',
    data={'task': 'something cool'}
    )
print("PUT({}): {}".format(ret.status_code, ret.json()))
ret = get ('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = post ('http://localhost:5000/todos', data={'task': 'cooltask'})
print("POST({}): {}".format(ret.status_code, ret.json()))

ret = get('http://localhost:5000/todos/todo1')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = delete('http://localhost:5000/todos/todo1')
print("DELETE({}): {}".format(
    ret.status_code,
    ret.text))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(
    ret.status_code,
    ret.json()))
