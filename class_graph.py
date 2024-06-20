import networkx as nx
import matplotlib.pyplot as plt
class graph:
    def __init__(self, adj_list):
        self.gdict = adj_list

    def Vertices(self):
        return list(self.gdict.keys())
    def Edges(self):
        edges=[]
        for k in self.gdict:
            for v in self.gdict[k]:
                edge=(k, v)
                edges.append(edge)
        return list(edges)
    def degree_vertex(self, v):
        return len(list(self.gdict[v]))
#create the dictionary with the graph elements
graph_adj_list={
    "a":["b", "c"],
    "b":["a", "c"],
    "c":["a", "d"],
    "d":["e"],
    "e":["d"]
}
g=graph(graph_adj_list)
print(g.Vertices())
print(g.Edges())
ver=input("enter the vertex to find degree ")
print(g.degree_vertex(ver))
G=nx.Graph()
G.add_edges_from(g.Edges())
nx.draw_networkx(G)
plt.show()