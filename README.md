# Communication With Server
1. Setting up : Static IP Address, DHCP range, server IP address and port, username, password
2. Configuration:
	* testuser
	* testadmin
3. Data to be uploaded:
	* Telemetry data(Latitude, Longitude, altitude, heading)
	* ODLC object and image (type, latitude, longitude, orientation, shape,
	  shape color, alphanumeric, alphanumeric color )
	* MAVLink commands
4. Extracting Data from the server:
	* Data to be extracted using endpoints
	* Status of teams
	* Mission : JSON response containing :
		* ID
		* flyzones - altitude , boundary points( latitude, longitude), waypoints (latitude,longitude,altitude),search grid points,air drop boundary points etc.

## SETUP
### Setting Up Host Computer

These installations are important, please install them before your proceed further.
1. docker- https://docs.docker.com/engine/install/
2. docker-compose - https://docs.docker.com/compose/install/
3. git - high chance you must have already installed this, needed for cloning repository and version changes. https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


Interop Git Repo - Clone the github repository git clone https://github.com/auvsi-suas/interop.git
Change directories - cd interop
Docker Images- The interop system is release to teams as these.
`auvsisuas/interop-server`

`cd interop/server`

`sudo ./interop-server.sh create_db`

`sudo ./interop-server.sh load_test_data`

`sudo ./interop-server.sh up`

(This will run the server, to exit Ctrl+C)


There are a few other commands here such as view server log, upgrade server log and delete server data but these can be skipped for now


`auvsisuas/interop-client`

`cd interop/client`
`sudo ./interop-client.sh run`
To request status of teams - ( Here the local ip of interop is required) which will be localhost:8000 so replace the server IP given in the code with localhost:8000

```
./tools/interop_cli.py \
    --url http://10.10.130.2:8000 \
    --username testuser \
    Teams
 ```

Similarly get mission
Upload objects
Check the folder structure, (2 json, 2 jpg)
Example command to upload
```
./tools/interop_cli.py \
    --url http://10.10.130.2:8000 \
    --username testuser \
    odlcs \
    --odlc_dir /path/to/object/directory
    
 ```


Mission configuration - just check admin web login, Navigate to http://localhost:8000
Interop Integration - with the interop server, is it needed? Quite similar to the initial set up, it is done using python scripts.


**API specification**:
Endpoints
Make get requests, some require json formatting, this is the most important part, will provide us with mission data
One of the examples.
GET /api/missions/1 HTTP/1.1
Host: 192.168.1.2:8000
Cookie: sessionid=9vepda5aorfdilwhox56zhwp8aodkxwi

* Competition host os is Ubuntu
* Username:testuser, password:testpass
* The router will be configured to have a static IP address range, and a DHCP IP address range

### API Specification
Terminal Commands:(https://adityasridhar.com/posts/how-to-easily-use-curl-for-http-requests )
1. Login to the server: `curl -v --header "Content-Type: application/json" -d " {\"username\":\"testadmin\",\"password\":\"testpass\"}" 
http://localhost:8000/api/login`
2. Getting response from server:
`curl -v --cookie "sessionid=6d68n8qysqjde3cvtp3dlbhezjhd3dwo" http://localhost:8000/api/teams`

3. Getting Mission Response:

`curl -v --cookie "sessionid=6d68n8qysqjde3cvtp3dlbhezjhd3dwo" http://localhost:8000/api/missions/1`

4. Upload Telemetry data

`curl -v --cookie "sessionid=6d68n8qysqjde3cvtp3dlbhezjhd3dwo" --header "Content-Type: application/json" -d "{\"latitude\":\"38\",\"longitude\":\"-75\",\"altitude\":\"50\",\"heading\":\"90\"}" http://localhost:8000/api/telemetry`

### Post And Get Using Python:

1. import requests(https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command )
2. For getting sessionID: `requests.Session()` (https://stackoverflow.com/questions/43716660/how-to-make-a-post-with-previous-cookies-with-python-requests-library-or-pycurl )

### Python script for logging in to server:-
1. Login to the server: 	
```
import requests
url = 'http://localhost:8000/api/login'
data = '{\"username\":\"testadmin\",\"password\":\"testpass\"}'
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=data, headers=headers) 	 	 	
print (req.text)
```

**With cookies**:
```
ses = requests.Session()  # use this object for all get / post requests #
r = ses.post(url, data=data,headers=headers)
```
2. Getting response from server:
```
import requests
ses=request.Session()
r1 = ses.get('http://localhost:8000/api/teams')
print(r1.text)

```
3. Getting Mission Response:
```
import requests
ses=request.Session()
r1 = ses.get('http://localhost:8000/api/missions/1')
print(r1.text)
```
4. Upload Telemetry data
```	 	
import requests
ses=requests.Session()
url = 'http://localhost:8000/api/telemetry'
data = '{\"latitude\":\"38\",\"longitude\":\"-75\",\"altitude\":\"50\",\"heading\":\"90\"}'
headers = {'Content-type': 'application/json'}
r = ses.post(url, data=data, headers=headers)
```

