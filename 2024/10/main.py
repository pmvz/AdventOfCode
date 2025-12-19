import numpy as np
import networkx as nx


array = np.genfromtxt("2024/10/input", delimiter=1, dtype=int)
graph = nx.DiGraph(array)

# Try to create a graph without any CS background
root_nodes = []
end_nodes = []

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        value = array[i,j]
        if value == 0:
            root_nodes.append((i,j))
        elif value == 9:
            end_nodes.append((i,j))

        # A node is connected to its neighbour if their value is one higher
        if i > 0 and array[i-1,j] == value + 1:
            graph.add_edge((i,j), (i-1,j))
        if i < array.shape[0]-1 and array[i+1, j] == value + 1:
            graph.add_edge((i,j), (i+1,j))
        if j > 0 and array[i,j-1] == value + 1:
            graph.add_edge((i,j), (i,j-1))
        if j < array.shape[1]-1 and array[i, j+1] == value + 1:
            graph.add_edge((i,j), (i,j+1))

# Part 1: trailhead scores
paths = 0
for root in root_nodes:
    for end in end_nodes:
        paths += nx.has_path(graph, root, end)

print(paths)

# Part 2: trail ratings
ratings = []
for root in root_nodes:
    rating = 0
    for end in end_nodes:
        rating += len(list(nx.all_simple_paths(graph, root, end)))
    ratings.append(rating)

print(sum(ratings))

