from requests import get,post,put


ret = put (
    "http://localhost:5000/todos/todo10",
    data=("task": "something cool")
    )
print("PUT({}): {}".format(ret.status_code,ret.json()))
ret = get ("http://localhost:5000/todos")
print("GET({}): {}".format(ret.status_code, ret.json()))
