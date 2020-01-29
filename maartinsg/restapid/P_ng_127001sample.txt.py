
from requests import get

ret = get('http://127.0.0.1:5000/ping/127.0.0.1')
print(("GET({}): {}".format(
    ret.status_code,
    ret.text))
