import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
fichier = 'experimentations_5G.csv'  # Assurez-vous que le fichier est dans le même répertoire ou précisez son chemin complet
donnée = pd.read_csv(fichier, encoding='cp1252', sep=';', quotechar='"')

print(donnée)

# Sélectionner les colonnes concernant les technologies
tech_colone = [col for col in donnée.columns if 'Techno' in col]
# Compter le nombre d'expérimentateurs utilisant chaque technologie
tech_usage = donnée[tech_colone].sum()
print(tech_usage)
# Trier les technologies par utilisation
tech_usage_sorted = tech_usage.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
tech_usage_sorted.plot(kind='bar', color='green')
plt.title('Technologies les plus utilisées par les expérimentateurs')
plt.xlabel('Technologies')
plt.ylabel("Nombre d'utilisations")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

plt.tight_layout()
plt.show()
