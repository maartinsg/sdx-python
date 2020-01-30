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

ret = get('http://127.0.0.1:5000/student/student1')
print("GET({}): {}".format(
    ret.status_code,
    ret.text))
