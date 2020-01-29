from requests import put, get

ret = put(
    'http://localhost:5000/todo1',
    data={'data': 'Remember me'}
         )
print("PUT(todo1): {}".format(ret.json()))
##print("PUT(todo1): {}".format(ret.text))

ret = get('http://localhost:5000/todo1')
print("GET(todo1): {}".format(ret.json()))

ret = put(
    'http://localhost:5000/todo2',
    data={'data': 'Change something'}
    )
print("PUT(todo2): {}".format(ret.json()))

ret = get('http://localhost:5000/todo2')
print("GET(todo2): {}".format(ret.json()))
