#!/usr/bin/env python

from requests import put, get, post

ret = put(
    'http://localhost:5000/todos/todo10',
    data={'task': 'maybe to create a datafile please'}
    )
print("PUT({}): {}".format(ret.status_code, ret.text))

ret = get('http://localhost:5000/todos/todos')
print("GET({}): {}".format(ret.status_code, ret.text))

#ret = put(
#    'http://localhost:5000/todo2',
#    data={'data': 'Change my brakepads please'}
#    )
#print("PUT(todo2): {}".format(ret.json()))

#ret = post('http://localhost:5000/todos')
#print("POST({}): {}".format(ret.status_code, ret.json()))