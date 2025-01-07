import csv, folium

m=folium.Map(
    max_bounds=True,
    zoom_start=6,
    location=(47, 1),
    )
fg=folium.FeatureGroup(name="Icon collection", control=False).add_to(m)

# Premièrement, on va ouvrir notre fichier csv
# On précisera que les lignes sont séparer par '' et les cases sont délimiter par ';'
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read=csv.reader(file, delimiter=';')
    #On va ensuite parcourir notre feuille csv : ligne par ligne
    for i, row in enumerate(read):
        if i!=0:
            folium.Marker(location=(float(row[6].replace(',','.')),float(row[7].replace(',','.')))).add_to(fg)

m.save("index.html")