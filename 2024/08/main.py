import numpy as np
from itertools import combinations


array = np.genfromtxt("2024/08/input", delimiter=1, dtype="<U1")
is_antinode = np.full_like(array, False, dtype=bool)
origin = np.zeros(2)

# Iterate over all pairs of anntennae of the same frequency
for freq in np.unique(array[array != "."]):
    antennae = np.argwhere(array == freq)
    for antenna_1, antenna_2 in combinations(antennae, 2):
        # Find the antinodes using basic vector math. In part 1, k is -1 and 2
        direction = antenna_2 - antenna_1
        k = np.arange(-max(array.shape), max(array.shape))
        antinodes = k[:,np.newaxis] * direction[np.newaxis,:] + antenna_1

        # Only keep antinodes within bounds and store their locations
        in_bounds = ((origin <= antinodes) & (antinodes < array.shape))
        antinodes_idx = np.argwhere(in_bounds.all(axis=1))
        is_antinode[*antinodes[antinodes_idx].T] = True


print(is_antinode.sum())
