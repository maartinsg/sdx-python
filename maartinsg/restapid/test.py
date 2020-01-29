#!/usr/bin/env python

from requests import put, get, post, delete

#ret = put(
#    'http://localhost:12345/todos/todo10',
#    data={'task': 'maybe to create a datafile please'}
#    )
#print("PUT({}): {}".format(ret.status_code, ret.text))

#ret = delete('http://127.0.0.1:12345/todos/todo10')
#print("DELETE({}): {}".format(
#    ret.status_code,
#    ret.text))

ret = get('http://127.0.0.1:5000/ping/127.0.0.1')
print("GET({}): {}".format(
    ret.status_code,
    ret.text))







#ret = put(
#    'http://localhost:5000/todo2',
#    data={'data': 'Change my brakepads please'}
#    )
#print("PUT(todo2): {}".format(ret.json()))

#ret = post('http://localhost:5000/todos')
#print("POST({}): {}".format(ret.status_code, ret.json()))