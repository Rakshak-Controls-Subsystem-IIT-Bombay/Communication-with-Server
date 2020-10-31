url = 'http://localhost:8000/api/telemetry'
data = '{\"latitude\":\"38\",\"longitude\":\"-75\",\"altitude\":\"50\",\"heading\":\"90\"}'
headers = {'Content-type': 'application/json'}
r = ses.post(url, data=data, headers=headers)
