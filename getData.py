from types import resolve_bases
import requests
import urllib.request
import json

# full url
# url = "http://openapi.seoul.go.kr:8088/464378587a72656131303254716d5443/json/bikeList/1/3/"
url = "http://openapi.seoul.go.kr:8088/"

# API params
KEY = '464378587a72656131303254716d5443'
TYPE = 'json'
SERVICE = 'bikeList'
START_INDEX = '1'
END_INDEX = '1000'

'''
rackTotCnt : 거치대 개수
stationName : 대여소 이름
parkingBikeTotCnt : 자전거 주차 총 건수
shared : 거치율
stationLatitude : 위도
stationLongitude : 경도
stationId : 대여소 ID
'''

URL = url + KEY + '/' + TYPE + '/' + SERVICE + '/' + START_INDEX + '/' + END_INDEX + '/'

myurl = urllib.request.urlopen(URL)
data = str(json.loads(myurl.read().decode('utf-8')))

if data.find("INFO-000"):
    start = data.find('[')
    end = data.find(']')
    data = data[start:end+1].replace("'", '"')

with open("/data/project/data.json", "w") as f:
    f.write(data)
