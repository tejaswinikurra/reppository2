import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
#G.add_nodes_from([1, 2, 3])
path_graph  = nx.path_graph(10)
nx.draw(G, with_labels = True, font_color = 'whitesmoke')
plt.show()

