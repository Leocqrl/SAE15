import csv

# Premièrement, on va ouvrir notre fichier csv
# On précisera que les lignes sont séparer par '' et les cases sont délimiter par ';'
with open('experimentations_5G.csv', newline='') as file:
    read=csv.reader(file, delimiter=';')
    #On va ensuite parcourir notre feuille csv : ligne par ligne
    for row in read:
        ...
        


# Position [latitude, longitude] sur laquelle est centrée la carte
location = [47, 1]

# Niveau de zoom initial
zoom = 6

# Style de la carte
tiles = 'cartodbpositron'

# Création de la carte
Carte = folium.Map(location=location,
                   zoom_start=zoom,
                   tiles=tiles)

# Sauvegarde dans un fichier HTML
Carte.save('carte_interactive.html')

print("Carte enregistrée sous 'carte_interactive.html'")
