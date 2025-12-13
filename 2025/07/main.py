import numpy as np


with open("Day 7/input") as file:
    lines = file.readlines()

# Originally loaded as an array of characters, but converted to int for step 2
manifold = np.array([[char for char in line if char != '\n'] for line in lines])
manifold_num = np.zeros_like(manifold, dtype=np.int64)
manifold_num[manifold == 'S'] = 1
manifold_num[manifold == '^'] = -1

splits = 0
for i, row in enumerate(manifold_num[1:]):
    # Find for which indices the previous row had an S or |
    previous = np.argwhere(manifold_num[i] > 0).flatten()
    for j in previous:
        # Split the beam into a left and right beam if it encounters a ^
        if row[j] == -1:
            splits += 1
            row[j-1] += manifold_num[i,j]
            row[j+1] += manifold_num[i,j]
        # Otherwise the beam continues downward
        else:
            row[j] += manifold_num[i,j]

print(splits)
print(np.sum(manifold_num[-1]))
