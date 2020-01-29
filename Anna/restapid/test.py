from requests import get, put, post

ret = put(
    'http://localhost:5000/todos/todo10',
    data={'task': 'something cool'}
    )
print("PUT({}): {}".format(ret.status_code, ret.text))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.text))
