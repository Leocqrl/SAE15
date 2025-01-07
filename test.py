import csv, folium, branca
from folium.plugins import MarkerCluster

m=folium.Map(
    max_bounds=True,
    zoom_start=6,
    location=(47, 1),
    )
Marker_Cluster=MarkerCluster(name="Icon collection", control=False).add_to(m)

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

            #On met dans la variable html les informations que l'on veut lorsque l'on clique sur chaque Marker un a un
            html=f"""
            <h5>{row[0]}</h5>
            <FONT size="1px">
            <p>Bande de fréquences : {row[1]}</p>
            </FONT>
            """
            taille=100
            compteur=0
            for y in range(15, 32):
                if int(row[y])==1:
                    taille+=20
                    compteur+=1
                    if compteur==1:
                        html+=f"""
                        <FONT size="1px">
                        <h6>Recherche et Développement :</h6>
                        </FONT>
                        """
                    html+=f"""
                    <FONT size="1px">
                    <p>{Legende[y]}</p>
                    </FONT>
                    """  
                    
            iframe=branca.element.IFrame(html, width=150, height=taille)
            Popup=folium.Popup(iframe, max_width=500, max_height=300 )
            if compteur>=4:
                ICON=folium.Icon(color='red')
            elif 4>compteur>=2:
                ICON=folium.Icon(color='lightred')
            elif compteur==1:
                ICON=folium.Icon(color='orange')
            elif compteur==0:
                ICON=folium.Icon(color='lightgray')
            #Création du marker avec toute les informations précédentes
            folium.Marker(location=(lat,lon), popup=Popup, icon=ICON).add_to(Marker_Cluster)
        else :
            Legende=row

m.save("Carte_Interactive.html")