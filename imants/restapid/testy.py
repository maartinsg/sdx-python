#!/usr/bin/env python
from requests import get, post

ret = get ('http://localhost:5000/todos')
print("GET{{}}: {}".format(ret.status_code, ret.text))

ret = post ('http://localhost:5000/todos', data={'task': 'cooltask'})
print("POST{{}}: {}".format(ret.status_code, ret.text))
