import networkx as nx
import matplotlib.pyplot as plt
import random

# Créer un graphe non orienté avec un nombre aléatoire de sommets entre 2 et 15
num_nodes = random.randint(2, 15)
G_random = nx.Graph()
G_random.add_nodes_from(range(num_nodes))

# Ajouter des arêtes de manière aléatoire
# Pour chaque paire de nœuds, décider aléatoirement si une arête doit être ajoutée
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.choice([True, False]):
            G_random.add_edge(i, j)

# Tracer le graphe
nx.draw(G_random, with_labels=True)
plt.show()
