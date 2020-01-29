from requests import get, delete

'''
ret = delete('http://localhost:5000/todos/todo1')
print("DELETE({}): {}".format(
    ret.status_code,
    ret.text))
'''

ret = get('http://192.168.8.104:5000/TODOS/todo2')
print("GET({}): {}".format(
    ret.status_code,
    ret.text))
