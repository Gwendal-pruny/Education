# Importation des bibliothèques nécessaires pour la manipulation de graphes et la visualisation
import matplotlib.pyplot as plt
import networkx as nx
from numpy import array

# Définition du graphe
G = nx.Graph() # Crée une nouvelle instance d'un graphe non orienté

# Définition des n?uds avec leurs attributs
G.add_node(0, label='A', col='pink')   # Ajoute le n?ud 0 avec un label 'A' et une couleur 'pink'
G.add_node(1, label='B', col='red')    # Ajoute le n?ud 1 avec un label 'B' et une couleur 'red'
G.add_node(2, label='C', col='white')  # Ajoute le n?ud 2 avec un label 'C' et une couleur 'white'
G.add_node(3, label='D', col='white')  # Ajoute le n?ud 3 avec un label 'D' et une couleur 'white'
G.add_node(4, label='E', col='white')  # Ajoute le n?ud 4 avec un label 'E' et une couleur 'white'
G.add_node(5, label='F', col='blue')   # Ajoute le n?ud 5 avec un label 'F' et une couleur 'blue'

# Définition des arêtes avec leur poids
G.add_edge(0, 1, weight=6)  # Ajoute une arête entre le n?ud 0 et 1 avec un poids de 6
G.add_edge(0, 2, weight=5)  # Ajoute une arête entre le n?ud 0 et 2 avec un poids de 5
G.add_edge(0, 4, weight=1)  # Ajoute une arête entre le n?ud 0 et 4 avec un poids de 1

# Traitement des n?uds pour définir la couleur lors de la visualisation
colorList = [G.nodes[data]['col'] for node in G.nodes(data=True)] # Crée une liste des couleurs pour chaque n?ud

# Positionnement des n?uds pour l'affichage
pos = nx.spring_layout(G) # Utilise l'algorithme de positionnement 'spring_layout' pour le graphe G

# Dessin du graphe avec les n?uds colorés selon les attributs
nx.draw_networkx_nodes(G, pos, node_size=700, node_color=colorList, alpha=0.9) # Dessine les n?uds avec leur couleur et taille spécifiée

# Traitement des n?uds pour définir le label lors de la visualisation
labels_nodes = {node[0]:node[1]['label'] for node in G.nodes(data=True)} # Crée un dictionnaire des labels pour chaque n?ud

# Dessin des labels des n?uds
nx.draw_networkx_labels(G, pos, labels=labels_nodes, font_size=20, font_color='black', font_family='sans-serif') # Dessine les labels des n?uds

# Traitement des arêtes pour définir le label (poids) lors de la visualisation
labels_edges = {edge:G.edges[edge]['weight'] for edge in G.edges()} # Crée un dictionnaire des poids pour chaque arête

# Dessin des arêtes et des labels de poids
nx.draw_networkx_edges(G, pos, width=1) # Dessine les arêtes
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edges, font_color='red') # Dessine les labels des arêtes avec le poids

# Affichage du graphe
plt.axis('off') # Désactive les axes pour un affichage plus propre
plt.show() # Montre le graphe dessiné