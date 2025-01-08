import csv
import pandas as pd
from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.title("Tableau des entreprises par région")
colonne = ("Région", "Entreprises")
tableau = ttk.Treeview(fenetre, columns=colonne, show="headings")
tableau.column("Région", width=200)
tableau.column("Entreprises", width=800)
tableau.heading("Région",text="Région")
tableau.heading("Entreprises",text="Entreprises")
# Création d'un dictionnaire qui va contenir une liste d'entreprises pour chaque région
regions_dict ={}
# Ouverture du fichier CSV
with open('experimentations_5G.csv', newline='', encoding='cp1252') as file:
    read = csv.reader(file, delimiter=';')
    # Parcours du fichier CSV ligne par ligne
    for i, row in enumerate(read):
        if i!=0:
            entreprise = row[0]  # Entreprise (colonne 0)
            lat=float(row[6].replace(',','.'))
            lon=float(row[7].replace(',','.'))
            if row[11]!='':
                region = row[11]     # Région (colonne 11)
            else : 
                region= row[10]
            # Ajouter l'entreprise à la liste correspondant à la région
            if region not in regions_dict :
                regions_dict[region]=[]
            if entreprise not in regions_dict[region]:
                regions_dict[region].append(entreprise)
df = pd.DataFrame({
    'Région': regions_dict.keys(),
    'Entreprise': regions_dict.values()
})

df = df.sort_values(by='Région').reset_index(drop=True)
for index, row in df.iterrows():
    region = row['Région']
    entreprises = ", ".join(row['Entreprise'])
    tableau.insert("", "end", values=(region, entreprises))

tableau.pack(padx=20, pady=20)
fenetre.mainloop()