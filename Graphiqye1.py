import pandas as pd
import matplotlib.pyplot as plt

# Charger les données avec les paramètres spécifiques
fichier = 'experimentations_5G.csv'
donnée = pd.read_csv(fichier, encoding='cp1252', sep=';', quotechar='"')

# Vérifier les colonnes disponibles
print(donnée)

# Exemple : Compter le nombre d'expérimentations par région
experimentateur_region = donnée['Région'].value_counts()
# l'option value_counts compte le nombre ou une valeur dans la serie Région se répéte.
print(experimentateur_region)
# Créer un histogramme
plt.figure(figsize=(10, 5))
experimentateur_region.plot(kind='bar', color='red')
plt.title('Nombre d\'expérimentations 5G par région')
plt.xlabel('Région')
plt.ylabel('Nombre d\'expérimentations')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Afficher le graphique
plt.tight_layout() 
plt.show()










