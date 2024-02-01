import networkx as nx
import matplotlib.pyplot as plt

# Création d'un graphe non orienté
G = nx.Graph() # 1. Création du graphe G

# Ajout de sommets nommés 1, 2, 3, 4 et 5
G.add_nodes_from([1, 2, 3, 4, 5]) # 2. Ajout des sommets 1, 2, 3, 4 et 5 au graphe G

# Ajout d'arêtes avec des poids
G.add_edge(2, 3, weight=1) # 5. Ajout de l'arête {2, 3} au graphe G avec un poids de 1
G.add_edge(2, 5, weight=3) # 5. Ajout de l'arête {2, 5} au graphe G avec un poids de 3
G.add_edge(3, 4, weight=4) # 5. Ajout de l'arête {3, 4} au graphe G avec un poids de 4
G.add_edge(4, 5, weight=2) # 5. Ajout de l'arête {4, 5} au graphe G avec un poids de 2

# Suppression du sommet 1
G.remove_node(1) # 4. Suppression du sommet 1 du graphe G

# Création d'un graphe orienté
DG = nx.DiGraph() # 1. Création du graphe orienté DG

# Ajout des mêmes sommets et arêtes au graphe orienté
DG.add_nodes_from([1, 2, 3, 4, 5]) # 2. Ajout des sommets 1, 2, 3, 4 et 5 au graphe DG
DG.add_weighted_edges_from([(1, 3, 2), (3, 2, 4), (2, 5, 5), (4, 5, 1)]) # 6. Ajout des arêtes (1,3), (3,2), (2,5), (4,5) au graphe DG avec leurs poids respectifs

# 3. Affichage des sommets des graphes
print("Sommets du graphe G : ", G.nodes())
print("Sommets du graphe DG : ", DG.nodes())

# 7. Tracer le graphe G et le graphe DG
nx.draw(G, with_labels=True)
plt.show()
nx.draw(DG, with_labels=True)
plt.show()