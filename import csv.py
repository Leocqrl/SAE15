import csv
import pandas as pd
from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.title("Tableau des entreprises par région")
colonne = ("Région", "Entreprises")
tableau = ttk.Treeview(fenetre, columns=colonne, show="headings")


tableau.heading("Région", text="Région")
tableau.heading("Entreprises", text="Entreprises")

# Définir les largeurs des colonnes
tableau.column("Région", width=150)
tableau.column("Entreprises", width=300)

# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict = {}

# Ouverture du fichier CSV
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    # Parcours du fichier CSV ligne par ligne
    for i, row in enumerate(read):
        if i != 0:  # Ignorer la première ligne (entêtes)
            entreprise = row[0]  # Entreprise (colonne 0)
            lat = float(row[6].replace(',', '.'))
            lon = float(row[7].replace(',', '.'))
            region = row[11] if row[11] != '' else row[10]  # Région (colonne 11 ou 10)
            
            # Ajouter l'entreprise à la liste correspondant à la région
            if region not in regions_dict:
                regions_dict[region] = []
            if entreprise not in regions_dict[region]:
                regions_dict[region].append(entreprise)

# Créer un DataFrame à partir du dictionnaire pour faciliter l'insertion des données dans le tableau
df = pd.DataFrame({
    'Région': regions_dict.keys(),
    'Entreprises': regions_dict.values()
})

# Trier le DataFrame par région
df = df.sort_values(by='Région').reset_index(drop=True)

# Insérer les données dans le tableau
for _, row in df.iterrows():
    region = row['Région']
    entreprises = ", ".join(row['Entreprises'])  # Joindre les entreprises par une virgule
    tableau.insert("", "end", values=(region, entreprises))

# Ajouter le Treeview à la fenêtre principale
tableau.pack(padx=20, pady=20)

# Lancer la boucle principale de Tkinter
fenetre.mainloop()
