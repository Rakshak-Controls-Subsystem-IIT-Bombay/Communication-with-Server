import requests
ses = requests.Session()
url = 'http://localhost:8000/api/login'
data = '{\"username\":\"testadmin\",\"password\":\"testpass\"}'
headers = {'Content-type': 'application/json'}
r = ses.post(url, data=data,headers=headers)

print(req.text)
print(ses.cookies.get_dict())


