import networkx as nx
from functools import cache


with open("Day 11/input") as file:
    lines = file.readlines()
    

# Part 1
# Construct the directed graph from the input
graph = nx.DiGraph()
for line in lines:
    source, destinations = line.split(':')
    for destination in destinations.split():
        graph.add_edge(source, destination)

# Find and count the paths from "you" to "out"
print(len(list(nx.all_simple_paths(graph, "you", "out"))))


# Part 2
# First attempt was the same as above, for each section svr-fft, fft-dac, dac-out
# and cutoffs set to the generations between svr-fft and fft-dac as determined from
# nx.topological_generations. Was way too slow but could not think of something else,
# instead found a recursive solution by derailed-dash that this is based on

@cache
def count_paths(graph, current, end_node):
    "Recursively search 'graph' and count how many times 'end_node' is reached"
    if current == end_node:  # Endpoint found
        return 1
    
    paths = 0
    # Outgoing paths must either lead to the end node, 
    # or lead to a node that has no outgoing neighbours.
    for successor in graph.successors(current):
        paths += count_paths(graph, successor, end_node)

    return paths


if nx.has_path(graph, "dac", "fft"):  # dac comes before fft
    total_paths = count_paths(graph, "svr", "dac")
    total_paths *= count_paths(graph, "dac", "fft")
    total_paths *= count_paths(graph, "fft", "out")
    print(total_paths)
else:  # fft comes before dac
    total_paths = count_paths(graph, "svr", "fft")
    total_paths *= count_paths(graph, "fft", "dac")
    total_paths *= count_paths(graph, "dac", "out")
    print(total_paths)