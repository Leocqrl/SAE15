import csv
L=[]
# Premièrement, on va ouvrir notre fichier csv
# On précisera que les lignes sont séparer par '' et les cases sont délimiter par ';'
with open('experimentations_5G.csv', newline='',encoding='cp1252') as file:
    read=csv.reader(file, delimiter=';')
    #On va ensuite parcourir notre feuille csv : ligne par ligne
    for row in read:
        if row == '':
            pass
        else:
            L.append([row[0],row[11]])

print(L)