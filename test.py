import csv, folium, branca

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
        #On va retirer la première ligne afin de ne pas être déranger par le nom des colonnes
        if i!=0:
            #On va ensuite mettre en float et remplacer les ',' par des '.' pour ne pas avoir d'erreur
            lat=float(row[6].replace(',','.'))
            lon=float(row[7].replace(',','.'))
            #On met dans la variable texte les informations que l'on veut lorsque l'on clique sur chaque Marker un a un
            html=f"""
            <h5>{row[0]}</h5>
            <FONT size="2px">
            <p>Bande de fréquences : {row[1]}</p>
            </FONT>
            """
            #Création du marker avec toute les informations précédentes
            folium.Marker(location=(lat,lon), popup=folium.Popup(branca.element.IFrame(html, 125, 75), max_width=125)).add_to(fg)

m.save("Carte_Interactive.html")