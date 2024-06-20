import networkx as nx
import matplotlib.pyplot as plt
import smoke

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G = nx.path_graph(10)
nx.draw(G, with_labels = True, font_color = 'white_smoke')
plt.show()

