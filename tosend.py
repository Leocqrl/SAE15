import csv, folium, branca, pandas as pd, matplotlib.pyplot as plt
from folium.plugins import MarkerCluster
from tkinter import *
from tkinter import ttk

#Tableau 1
fenetre = Tk()
fenetre.title("Tableau des acteurs engagés par région")
colonne = ("Région", "Acteurs engagés")
tableau = ttk.Treeview(fenetre, columns=colonne, show="headings")
tableau.column("Région", width=200)
tableau.column("Acteurs engagés", width=800)
tableau.heading("Région",text="Région")
tableau.heading("Acteurs engagés",text="Acteurs engagés")

#Carte interactive
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
# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict ={}
# Premièrement, on va ouvrir notre fichier csv
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    # On va ensuite parcourir notre feuille csv : ligne par ligne
    for i, row in enumerate(read):
        if i != 0:
            entreprise = row[0]  # Entreprise (colonne 0)
            lat = float(row[6].replace(',', '.'))
            lon = float(row[7].replace(',', '.'))
            if row[11]!='':
                region = row[11]     # Région (colonne 11)
            else : 
                region= row[10]
            # Ajouter l'entreprise à la liste correspondant à la région
            if region not in regions_dict :
                regions_dict[region]=[]
            if entreprise not in regions_dict[region]:
                regions_dict[region].append(entreprise)
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

# Tableau 1
df = pd.DataFrame({
    'Région': regions_dict.keys(),
    'Acteurs engagés': regions_dict.values()
})

df = df.sort_values(by='Région').reset_index(drop=True)
for index, row in df.iterrows():
    region = row['Région']
    entreprises = ", ".join(row['Acteurs engagés'])
    tableau.insert("", "end", values=(region, entreprises))

tableau.pack(padx=20, pady=20)
fenetre.mainloop()

###   Graph 1 :
# Charger les données avec les paramètres spécifiques
file_path = 'experimentations_5G.csv'
data = pd.read_csv(file_path, encoding='cp1252', sep=';', quotechar='"')

# Vérifier les colonnes disponibles
print(data.columns)

# Exemple : Compter le nombre d'expérimentations par région
experiments_by_region = data['Région'].value_counts()

# Créer un histogramme
plt.figure(figsize=(10, 6))
experiments_by_region.plot(kind='bar', color='red')
plt.title('Nombre d\'expérimentations 5G par région')
plt.xlabel('Région')
plt.ylabel('Nombre d\'expérimentations')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Afficher le graphique
plt.tight_layout()
plt.show()


### Graph 2
# Compter les sites par entreprise
site_counts = data.groupby('Expérimentateur').size().reset_index(name='Nombre de sites')

# Trier les entreprises par nombre de sites (ordre décroissant)
site_counts = site_counts.sort_values(by='Nombre de sites', ascending=False)

# Sélectionner les 10 premières entreprises pour le camembert
top_companies = site_counts[:10]
other_sites_count = site_counts['Nombre de sites'][10:].sum()

# Ajouter une catégorie "Autres" pour regrouper les entreprises restantes
labels = list(top_companies['Expérimentateur']) + ['Autres']
sizes = list(top_companies['Nombre de sites']) + [other_sites_count]

# Couleurs personnalisées pour une meilleure distinction
colors = plt.cm.tab10.colors[:len(labels)]

# Tracer le camembert
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 12},
    pctdistance=0.85  # Ajuste la position des pourcentages
)

# Ajouter un cercle pour créer un effet de "donut"
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Titre et style
plt.title('Répartition des sites par entreprise (Top 10)', fontsize=16)
plt.tight_layout()
plt.show()

# Sélectionner les colonnes concernant les technologies
tech_columns = [col for col in data.columns if 'Techno' in col]

# Compter le nombre d'expérimentateurs utilisant chaque technologie
tech_usage = data[tech_columns].sum()

# Trier les technologies par utilisation
tech_usage_sorted = tech_usage.sort_values(ascending=False)


plt.figure(figsize=(12, 6))
tech_usage_sorted.plot(kind='bar', color='royalblue')
plt.title('Technologies les plus utilisées par les expérimentateurs')
plt.xlabel('Technologies')
plt.ylabel("Nombre d'utilisations")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

plt.tight_layout()
plt.show()

