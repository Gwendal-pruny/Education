import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# Add edges to form a square and a cross
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)]
G.add_edges_from(edges)

# Draw the graph
pos = {1: [0, 0], 2: [1, 0], 3: [1, 1], 4: [0, 1], 5: [0.5, 0.5]}  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1200)

plt.show()