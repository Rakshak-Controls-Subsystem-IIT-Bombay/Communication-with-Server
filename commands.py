import requests
import json
ses = requests.Session()
###login to server##############################################
url_login = 'http://localhost:8000/api/login'
data = '{\"username\":\"testadmin\",\"password\":\"testpass\"}'
headers = {'Content-type': 'application/json'}
r_login = ses.post(url_login, data=data, headers=headers)
print(r_login.text)
###############################################################
###getting response from server################################
url_response='http://localhost:8000/api/teams'
r_response = ses.get(url_response)
print(r_response.text)
###############################################################
###getting mission response####################################
url_mission='http://localhost:8000/api/missions/1'
r_mission = ses.get(url_mission)
print(r_mission.text)
###############################################################
####upload telemetry data######################################
url_telemetry = 'http://localhost:8000/api/telemetry'
data = '{\"latitude\":\"38\",\"longitude\":\"-75\",\"altitude\":\"50\",\"heading\":\"90\"}'
headers = {'Content-type': 'application/json'}
r_telemetry = ses.post(url_telemetry, data=data, headers=headers)
print(r_telemetry.text)
###############################################################
file1=open('uav_login.json','w')
file1.write(r_login.text+'\n')
file1.close()

file2=open('uav_response.json','w')
file2.writelines(r_response.text+'\n')
file2.close()

file3=open('uav_mission.json','w')
file3.writelines(r_mission.text+'\n')
file3.close()

file4=open('uav_telemetry.json','w')
file4.writelines(r_telemetry.text+'\n')
file4.close()
