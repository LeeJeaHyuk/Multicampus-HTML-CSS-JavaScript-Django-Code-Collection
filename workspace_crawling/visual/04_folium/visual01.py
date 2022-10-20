import  folium

# 37.34635118,126.98146812
#zoom_start : 0 ~ 18
my_loc = folium.Map(location=[37.34635118,126.98146812], zoom_start=18)
my_loc.save('visual01.html')

