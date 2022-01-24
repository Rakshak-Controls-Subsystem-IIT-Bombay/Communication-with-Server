# Calculate maximum distance between four co-ordinates of the polygon 
# in which UGV will land, for power consumption estimation

# Requires uav_mission.json file to calculate the distance between coordinates

import json
from geopy.distance import vincenty

# Opening JSON file
f = open('uav_mission.json')
# returns JSON object as a dictionary
data = json.load(f)

# list to store individual coordinates and distances
latitude = []
longitude = []
coords = []
distance = []

# Iterating through the json list and storing it in separate list named coords
for i in data['airDropBoundaryPoints']:
  coords.append(i)

# storing individual latitudes and longitudes
for i in range(4):
  latitude.append(coords[i]['latitude'])
  longitude.append(coords[i]['longitude'])

# calculate distance between all possible combination of coordinates
for i in range(4):
  for j in range(4):
    if i!=j :
      coords_1 = (latitude[i], longitude[i])
      coords_2 = (latitude[j], longitude[j])
      distance.append(vincenty(coords_1, coords_2).km)
print("Max distance:", max(distance),"km")

# Closing file
f.close()