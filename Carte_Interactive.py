import csv, folium, branca
from folium.plugins import MarkerCluster

m = folium.Map(
    max_bounds=True,
    zoom_start=6,
    location=(47, 1),
)

Marker_Cluster = MarkerCluster(name="Icon collection", control=False).add_to(m)

## Ajout de la légende en bas à gauche (modifiée pour inclure les entreprises)
legend_html = """
    <div style="
        position: fixed; 
        bottom: 30px; 
        left: 30px; 
        width: 250px; 
        background: linear-gradient(to bottom, #f9f9f9, #e0e0e0); 
        border-radius: 8px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        padding: 15px; 
        font-size: 13px; 
        font-family: Arial, sans-serif; 
        color: #333;
        border: 1px solid #ccc;
        z-index:9999;
    ">
        <h4 style="margin-top: 0; font-size: 16px; text-align: center; color: #444;">Légende</h4>
        <hr style="border: none; height: 1px; background: #ccc; margin: 10px 0;">
        <h5 style="margin-top: 0; font-size: 14px; color: #444;">Nombre d'expérimentations</h5>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: red; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>4 ou plus</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: lightcoral; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>2-3</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: orange; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>1</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="background-color: lightgray; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>0</span>
        </div>
        <h5 style="margin-top: 10px; font-size: 14px; color: #444;">Nombre d'entreprises par zone</h5>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: orange; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>100 ou plus</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: yellow; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>10-100</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="background-color: green; width: 20px; height: 20px; border-radius: 50%; margin-right: 10px;"></div>
            <span>2-10</span>
        </div>
    </div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

m.get_root().html.add_child(folium.Element('''
    <link rel="icon" type="image/png" href="https://media.istockphoto.com/id/953455882/fr/vectoriel/ic%C3%B4ne-de-la-carte-image-vectorielle-dune-icone-de-localisation-pointeur-de-recherche-sur.jpg?s=612x612&w=0&k=20&c=lcnFx1X_Td0y-TU7uQ6RfbPcW1dX9fLTboVCuhlCVzw=" />
'''))

m.get_root().html.add_child(folium.Element('<title>Carte Interactive</title>'))

# Premièrement, on va ouvrir notre fichier csv
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    # On va ensuite parcourir notre feuille csv : ligne par ligne
    for i, row in enumerate(read):
        if i != 0:
            lat = float(row[6].replace(',', '.'))
            lon = float(row[7].replace(',', '.'))

            html = f"""
            <h5>{row[0]}</h5>
            <FONT size="1px">
            <p>Bande de fréquences : {row[1]}</p>
            </FONT>
            """
            taille = 100
            compteur = 0
            for y in range(15, 32):
                if int(row[y]) == 1:
                    taille += 20
                    compteur += 1
                    if compteur == 1:
                        html += f"""
                        <FONT size="1px">
                        <h6>Recherche et Développement :</h6>
                        </FONT>
                        """
                    html += f"""
                    <FONT size="1px">
                    <p>{Legende[y]}</p>
                    </FONT>
                    """
            
            iframe = branca.element.IFrame(html, width=150, height=taille)
            Popup = folium.Popup(iframe, max_width=500, max_height=300)

            if compteur >= 4:
                ICON = folium.Icon(color='red')
            elif 4 > compteur >= 2:
                ICON = folium.Icon(color='lightred')
            elif compteur == 1:
                ICON = folium.Icon(color='orange')
            elif compteur == 0:
                ICON = folium.Icon(color='lightgray')

            folium.Marker(location=(lat, lon), popup=Popup, icon=ICON).add_to(Marker_Cluster)
        else:
            Legende = row

m.save("Carte_Interactive.html")
