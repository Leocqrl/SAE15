import csv

# Premièrement, on va ouvrir notre fichier csv
# On précisera que les lignes sont séparer par '' et les cases sont délimiter par ';'
with open('experimentations_5G.csv', newline='') as file:
    read=csv.reader(file, delimiter=';')
    #On va ensuite parcourir notre feuille csv : ligne par ligne
    for row in read:
        if row == '':
            pass
        else:
            print(row[0],row[11])
