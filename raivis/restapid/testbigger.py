#!/usr/bin/env python
from requests import get, post

ret = get('http://localhost:5000/TODOS')
print("GET({}): {}".format(ret.status_code, ret.json()))

ret = post('http://localhost:5000/TODOS', data={'task': 'cool task'})
print("POST({}): {}".format(ret.status_code, ret.json()))
