import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = 'experimentations_5G.csv'  # Assurez-vous que le fichier est dans le même répertoire ou précisez son chemin complet
data = pd.read_csv(file_path, encoding='cp1252', sep=';', quotechar='"')

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
