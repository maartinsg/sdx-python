import requests
url = 'http://www.google.com'
r = requests.get(url)
print ("URL :" + str(url))
print ("staus :" + str(r.status_code))
print ("header : " + str(r.headers['content-type']))
print("Encoding : " + str(r.encoding))
print("body : [1,200]...".format(r.text))
