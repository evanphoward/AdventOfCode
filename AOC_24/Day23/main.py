from MiscFiles.library import *

inp = get_input(2024, 23).split("\n")
G = nx.Graph()
for line in inp:
    x, y = line.split('-')
    G.add_edge(x, y)

three_cliques = set()
biggest_clique = []
for clique in nx.find_cliques(G):
    if len(clique) > len(biggest_clique):
        biggest_clique = clique
    for three_clique in itertools.combinations(clique, 3):
        three_cliques.add(tuple(sorted(three_clique)))


print("Part 1:", sum(any(x[0] == 't' for x in three_clique) for three_clique in three_cliques))
print("Part 2:", ','.join(sorted(biggest_clique)))