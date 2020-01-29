from requests import post, get, put, delete

##ret = delete('http://localhost:5000/todos/todo1')
##print("DELETE({}): {}".format(ret.status_code, ret.text))

##ret = put(
##    'http://localhost:5000/todos/todo15',
##    data={'task': 'somthing coool15'}
##    )
##print("PUT({}): {}".format(ret.status_code, ret.json()))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))



