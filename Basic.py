
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G = nx.path_graph(10)
nx.draw(G, with_lables=True, font_color='whitesmoke')
plt.show()
