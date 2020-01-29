from requests import get

'''
ret = delete('http://localhost:5000/todos/todo1')
print("DELETE({}): {}".format(
    ret.status_code,
    ret.text))
'''

ret = get('http://localhost:5000/ping/192.168.8.104')
print("GET({}): {}".format(
    ret.status_code,
    ret.json()))
