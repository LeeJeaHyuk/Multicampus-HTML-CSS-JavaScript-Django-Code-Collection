import  folium

# 37.34635118,126.98146812
#zoom_start : 0 ~ 18
my_loc = folium.Map(location=[37.34635118,126.98146812], zoom_start=18)
folium.Marker([37.34635118,126.98146812], popup=folium.Popup('팝업', max_width=100)).add_to(my_loc)
my_loc.save('visual02.html')

