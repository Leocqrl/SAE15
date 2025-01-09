import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
data = pd.read_csv('experimentations_5G.csv', encoding='cp1252', sep=';', quotechar='"')

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
