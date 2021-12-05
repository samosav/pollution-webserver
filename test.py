import requests

mydata = {'d': 555}
r = requests.get('http://127.0.0.1:5000/update', params=mydata)
print(r.status_code)
print(r.text)
