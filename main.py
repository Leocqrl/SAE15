import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('experimentations_5G.csv', encoding='cp1252', sep=';', quotechar='"')

# Regrouper les bandes de fréquences par entreprise en supprimant les doublons
grouped = data.groupby('Expérimentateur')['Bande de fréquences'].apply(set).reset_index()

# Transformer les ensembles en listes pour affichage
grouped['Bande de fréquences'] = grouped['Bande de fréquences'].apply(lambda x: ', '.join(sorted(x)))

# Tracer le graphique
plt.figure(figsize=(14, len(grouped) * 0.4))  # Taille dynamique basée sur le nombre d'entreprises

# Afficher les bandes de fréquences sous forme de barres horizontales
plt.barh(grouped['Expérimentateur'], [len(x.split(', ')) for x in grouped['Bande de fréquences']], color='steelblue')

# Configurer les étiquettes et le titre
plt.xlabel('Nombre de bandes de fréquences', fontsize=10 )
plt.ylabel('Entreprises (Expérimentateurs)', fontsize=10)
plt.title('Bandes de fréquences utilisées par entreprise')

# Ajuster les étiquettes pour éviter les chevauchements
plt.tight_layout()

# Afficher le graphique
plt.show()


