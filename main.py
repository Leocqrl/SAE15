import csv
import pandas as pd

# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict ={}
# Ouverture du fichier CSV
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    # Parcours du fichier CSV ligne par ligne
    for i, row in enumerate(read):
        if i!=0:
            entreprise = row[0]  # Entreprise (colonne 0)
            
            if row[11]!='':
                region = row[11]     # Région (colonne 11)
            else : 
                region= row[8]
            # Ajouter l'entreprise à la liste correspondant à la région
            if region in regions_dict and entreprise not in regions_dict[region]:
                regions_dict[region].append(entreprise)
            else :
                regions_dict[region]= [entreprise]
print(regions_dict)
print(len(regions_dict))

tableau = pd.DataFrame.from_dict(region_dict)
print(tableau)

# Affichage du dictionnaire des régions avec les entreprises
#for region, entreprises in regions_dict.items():
#    print(f"Région: {region}")
#    for entreprise in entreprises:
#        print(f"  - {entreprise}")
