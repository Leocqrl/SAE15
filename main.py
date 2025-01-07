import csv

# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict ={}
# Ouverture du fichier CSV
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    
    # Parcours du fichier CSV ligne par ligne
    for row in read:
        entreprise = row[0]  # Entreprise (colonne 0)
        region = row[11]     # Région (colonne 11)
            
        # Ajouter l'entreprise à la liste correspondant à la région
        
        



# Affichage du dictionnaire des régions avec les entreprises
#for region, entreprises in regions_dict.items():
#    print(f"Région: {region}")
#    for entreprise in entreprises:
#        print(f"  - {entreprise}")
