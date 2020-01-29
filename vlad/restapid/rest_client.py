from requests import get, post, put


#ret = get('http://localhost:5000/todos')
#print("GET({}): {}".format(ret.status_code, ret.json()))

#ret = post('http://localhost:5000/todos', data={'task': 'u can do better!!!!@!@!'})
#print("POST({}): {}".format(ret.status_code, ret.json()))

ret = put(
    'http://localhost:5000/todos/todo10',
    data={'task': 'something cool'}
    )

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.text))
