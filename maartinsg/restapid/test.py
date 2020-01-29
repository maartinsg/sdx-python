#!/usr/bin/env python

from requests import put, get, post

#ret = put(
#    'http://localhost:5000/todo1',
#    data={'data': 'Remember the milk please'}
#    )
#print("PUT(todo1): {}".format(ret.json()))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))

#ret = put(
#    'http://localhost:5000/todo2',
#    data={'data': 'Change my brakepads please'}
#    )
#print("PUT(todo2): {}".format(ret.json()))

ret = post('http://localhost:5000/todos')
print("POST({}): {}".format(ret.status_code, ret.json()))