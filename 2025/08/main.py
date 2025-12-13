import numpy as np
import networkx as nx


# Calculate all distances, set distances to self to NaN
boxes = np.loadtxt("Day 8/input", delimiter=',')
distances = np.linalg.norm(boxes[:,np.newaxis,:] - boxes[np.newaxis,:,:], axis=-1)
distances[np.diag_indices_from(distances)] = np.nan

# Sort the distances and return the indices as (i,j) pairs, skip b-a for every a-b (and a-a)
mindistances = np.array(np.unravel_index(np.argsort(distances, axis=None), distances.shape)).T
mindistances = mindistances[:-boxes.shape[0]:2]

# Construct a graph from the 1000 shortest edges between nodes
graph = nx.Graph()
graph.add_nodes_from(range(boxes.shape[0]))

for i in range(1000):
    graph.add_edge(*mindistances[i])

# Multiply the largest three subgraph sizes together -> part 1
subgraph_sizes = [len(sub) for sub in sorted(nx.connected_components(graph), key=len, reverse=True)]
print(np.prod(subgraph_sizes[:3]))

# Keep connecting until all nodes are connected
last_connection = None
for i in range(i+1, mindistances.shape[0]):
    graph.add_edge(*mindistances[i])
    
    if len([sub for sub in nx.connected_components(graph)]) == 1:
        last_connection = mindistances[i]
        break

# Multiply the x locations of the last connected nodes -> part 2
print(boxes[last_connection[0]][0] * boxes[last_connection[1]][0])
