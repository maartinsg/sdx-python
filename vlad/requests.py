import requests

url = 'http://www.google.com'
r = requests.get(url)
print("URL: " + str(url))
print("Status: " + str(r.status_code))
print("Header: " + str(r.headers['content-type']))
print("Encoding: " + str(r.encoding))
print("Body: {:.200}...".format(r.text))

