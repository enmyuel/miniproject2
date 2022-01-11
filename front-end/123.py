import folium

# MarkerCluster 실습을 위한 데이터
# 서울 따릉이 위치 정보
data = {'망원역 1번출구 앞':[37.55564880, 126.91062927],
        '망원역 2번출구 앞':[37.55495071, 126.91083527],
        '합정역 1번출구 앞':[37.55062866, 126.91498566],
        '합정역 5번출구 앞':[37.55000687, 126.91482544],
        '합정역 7번출구 앞':[37.54864502, 126.91282654],
        '신한은행 서교동금융센터점 앞':[37.55751038, 126.91850281],
        '서교동 사거리':[37.55274582, 126.91861725],
        '합정역 5번출구 앞':[37.55000687, 126.91482544],
   }

map1 = folium.Map(location =[37.566535, 126.9779691999996], 
       zoom_start = 10,
       zoom_control = False,
       control_scale = True, 
       tiles = 'OpenStreetMap') 
map1

# MarkerCluster 불러오기
from folium.plugins import MarkerCluster
marker_cluster = MarkerCluster().add_to(map1)

# 각각의 Marker을 MarkerCluster에 추가.
for msg, loc in data.items():
 # print(msg, loc)
 folium.Marker(location= loc, popup = folium.Popup(msg, max_width = 200)).add_to(marker_cluster)
 map1


map1.save('map.html')

 