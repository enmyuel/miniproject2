import json

# open json file
with open('/data/project/data.json') as json_file:
    json_data = json.load(json_file)

# get stationName, lat, lng data from json file and append to dict
def getStationData():
    data = dict()
    for i in json_data:
        stationName = i["stationName"]
        stationName = stationName[stationName.find('.')+1:].strip()
        latitude = i["stationLatitude"]
        longitude = i["stationLongitude"]
        data[stationName] = [float(latitude), float(longitude)]

    return data
