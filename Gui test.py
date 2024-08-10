import http.client
import json
conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "ffab3222fb57385dc0e67dd55d5e62507c1f0753c1d16dea15792e2d021cc2cf",
    'Content-type': "application/json"
    }

conn.request("GET", "/ndvi/latest/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

res = conn.getresponse()
data = res.read()

dtAM1 = data.decode("utf-8")
json_str = json.loads(dtAM1)

dtAM2 = json_str['data'][0]

ndvi= dtAM2['ndvi']
evi= dtAM2['evi']
summary= dtAM2['summary']
print(ndvi, evi, summary)

conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "ffab3222fb57385dc0e67dd55d5e62507c1f0753c1d16dea15792e2d021cc2cf",
    'Content-type': "application/json"
}

conn.request("GET", "/latest/pollen/by-lat-lng?lat={}&lng={}".format(lat, long), headers=headers)

res = conn.getresponse()
data = res.read()

apiAM = data.decode("utf-8")
json_str = json.loads(apiAM)
dt_AM_0 = json_str['data']
dt_AM1 = dt_AM_0[0]['Count']
dt_AM2 = dt_AM_0[0]['Risk']
grass_pollen_count = dt_AM1["grass_pollen"]
grass_pollen_risk = dt_AM2["grass_pollen"]
tree_pollen_count = dt_AM1["tree_pollen"]
tree_pollen_risk = dt_AM2["tree_pollen"]
weed_pollen_count = dt_AM1["weed_pollen"]
weed_pollen_risk = dt_AM2["weed_pollen"]

# Ambee
conn = http.client.HTTPSConnection("api.ambeedata.com")

headers = {
    'x-api-key': "ffab3222fb57385dc0e67dd55d5e62507c1f0753c1d16dea15792e2d021cc2cf",
    'Content-type': "application/json"
}

conn.request("GET", "/ndvi/latest/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

res = conn.getresponse()
data = res.read()

dtAM1 = data.decode("utf-8")
json_str = json.loads(dtAM1)

dtAM2 = json_str['data'][0]

ndvi = dtAM2['ndvi']
evi = dtAM2['evi']
summary = dtAM2['summary']
