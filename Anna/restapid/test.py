from requests import get, delete

ret = delete('http://localhost:5000/todos/todo1')
print("DELETE({}): {}".format(
    ret.status_code,
    ret.text))

ret = get('http://localhost:5000/todos')
print("GET({}): {}".format(
    ret.status_code,
    ret.text))
