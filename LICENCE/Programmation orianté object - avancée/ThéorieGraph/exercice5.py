import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(range(1, 10))

edges = [(1, 2, 2), (1, 3, 1), (2, 3, 2),(2, 7, 3), (2, 4, 1),(3, 5, 5),
         (4, 5, 3), (4, 6, 3), (5, 6, 1), (6, 7, 4),
         (6, 8, 1), (6, 9, 3), (7, 8, 5), (8, 9, 2),]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

pos = nx.spring_layout(G)  # positionnement des nœuds
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graphe avec Poids")
plt.show()

# Question 2: Écrire une fonction testnonisole
def test_non_isole(G):
    for node in G.nodes():
        if G.degree(node) == 0:
            return False
    return True

print(test_non_isole(G))

# Question 3: Expliquer ce que fait la fonction nx.cycle_basis
# La fonction nx.cycle_basis trouve une base pour les cycles d’un graphe non orienté.

# Question 4: Écrire une fonction AlgoACM
def AlgoACM(G):
    if nx.is_connected(G):
        T = nx.minimum_spanning_tree(G)
        poids = sum([data['weight'] for u, v, data in T.edges(data=True)])
        return T, poids
    else:
        return None, None

# Question 5: Appliquer cette fonction au graphe G précédent et représenter l'arbre couvrant de poids minimal obtenu
T, poids = AlgoACM(G)
if T is not None:
    print("Poids de l'arbre couvrant minimal :", poids)
    nx.draw(T, with_labels=True, font_size=10)
    plt.show()
else:
    print("Le graphe n'est pas connecté.")