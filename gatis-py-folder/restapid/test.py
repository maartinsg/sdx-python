from requests import post, get, put, delete

##ret = put(
##    'http://localhost:5000/todos/todo15',
##    data={'task': 'somthing coool 15'}
##    )
##print("PUT({}): {}".format(ret.status_code, ret.json()))

##ret = delete('http://localhost:5000/todos/todo15')
##print("DELETE({}): {}".format(ret.status_code, ret.text))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(ret.status_code, ret.json()))



