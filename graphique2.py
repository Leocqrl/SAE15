import pandas as pd
import matplotlib.pyplot as plt
# Charger le fichier CSV
donnée = pd.read_csv('experimentations_5G.csv', encoding='cp1252', sep=';', quotechar='"')
print(donnée)

# Compter les sites par entreprise

site_counts = donnée.groupby('Expérimentateur').size().reset_index(name='Nombre de sites')

print(site_counts)
# groupby() : permet de regrouper les données selon une ou plusieurs colonnes. 

# .size(): compte le nombre de lignes dans chaque groupe

# reset_index() : Convertit l'index des groupes en colonnes normales, créant un DataFrame.

# name='Nombre de sites' : Renomme la colonne contenant les tailles des groupes en "Nombre de site"

# Trier les entreprises par nombre de sites (ordre décroissant)

site_counts = site_counts.sort_values(by='Nombre de sites', ascending=False) 
#sort_values est une fonction qui permet de trié les données d'un Dataframe donc tableau.
#la fonction ascending=false false permet de trié par ordre décroissant 
# Sélectionner les 10 premières entreprises pour le camembert
top_companies = site_counts[:10]
other_sites_count = site_counts['Nombre de sites'][10:].sum()
# site_counts['nombre de sites']  permet d'utilisé seulement la colone Nombre de sites et de compté à partir de la 11éme ligne puis calculé la somme des sites qui se répéte à l'aide de la fonction sum()

# Ajouter une catégorie "Autres" pour regrouper les entreprises restantes
labels = list(top_companies['Expérimentateur']) + ['Autres']
sizes = list(top_companies['Nombre de sites']) + [other_sites_count]
print(sizes)
print(labels)
# Couleurs personnalisées pour une meilleure distinction
colors = plt.cm.tab10.colors[:len(sizes)]

# Tracer le camembert
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=0,
    colors=colors,
    textprops={'fontsize': 12}, #Ajuste la taille de la police
    pctdistance=0.9  # Ajuste la position des pourcentages
)

# Ajouter un cercle pour créer un effet de "donut"
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
plt.gca().add_artist(centre_circle)
# cette fonction nous as permis d'ajouter  un cercle vide dans notre cercle créer donc d'avoir un effet donuts

# Titre et style
plt.title('Répartition des sites par entreprise (Top 10)', fontsize=16)
plt.tight_layout() # ajuste automatiquement les marges et espacements des sous-graphiques pour éviter les chevauchements et optimiser la présentation.
plt.show()
