import folium
a=49.4783333333333
b=0.126111111111111
m=folium.Map(
    max_bounds=True,
    zoom_start=6,
    location=(47, 1),
    )
fg=folium.FeatureGroup(name="Icon collection", control=False).add_to(m)
folium.Marker(location=(a,b)).add_to(fg)

m.save("index.html")