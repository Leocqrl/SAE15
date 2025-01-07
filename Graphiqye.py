import pandas as pd
import matplotlib.pyplot as plt

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


