from requests import put, get, post

#version 3 updated
#ret = delete('http://localhost:5000/todos')
#print("delete({}): {}".format(ret.status_code, ret.json()))

ret = get('http://192.168.8.107:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))


"""
ret = put(
         'http://localhost:5000/todos'
         fdghfgh
         )
print("GET({}): {}".format(ret.status_code, ret.json()))
"""

"""
#version 3
ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))
"""
"""
#version 2
ret = get('http://localhost:5000/todos')
print("GET(todos): {}".format(ret.json()))

ret = post('http://localhost:5000/todos')
print("POST(todos): {}".format(ret.json()))
"""

"""
#version 1
ret = put(
    'http://localhost:5000/todo1',
    data={'data': 'Remember the milk'}
    )
print("PUT(todo1): {}".format(ret.json()))

ret = get('http://localhost:5000/todo1')
print("GET(todo1): {}".format(ret.json()))

ret = put(
    'http://localhost:5000/todo2',
    data={'data': 'Change my brakepads'}
    )
print("PUT(todo2): {}".format(ret.json()))

ret = get('http://localhost:5000/todo2')
print("GET(todo2): {}".format(ret.json()))
"""
