import csv
from collections import defaultdict

# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict = defaultdict(list)

# Ouverture du fichier CSV
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    
    # Parcours du fichier CSV ligne par ligne
    for row in read:
        # Vérifier si la ligne n'est pas vide
        if row:
            try:
                entreprise = row[0]  # Entreprise (colonne 0)
                region = row[11]     # Région (colonne 11)
                
                # Ajouter l'entreprise à la liste correspondant à la région
                regions_dict[region].append(entreprise)
            except IndexError:
                # Si la ligne ne contient pas suffisamment de colonnes, on passe à la suivante
                continue

# Affichage du dictionnaire des régions avec les entreprises
for region, entreprises in regions_dict.items():
    print(f"Région: {region}")
    for entreprise in entreprises:
        print(f"  - {entreprise}")
