import networkx as nx

G = nx.Graph()
for line in open("input").read().split("\n"):
    label, neighbors = line.split(": ")
    neighbors = neighbors.split()
    for n in neighbors:
        G.add_edge(u_of_edge=label, v_of_edge=n)

cut_edges = list(nx.minimum_edge_cut(G))
for edge in cut_edges:
    G.remove_edge(edge[0], edge[1])
print("Part 1:", len(nx.node_connected_component(G, cut_edges[0][0])) * len(nx.node_connected_component(G, cut_edges[0][1])))