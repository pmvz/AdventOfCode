import numpy as np


# Part 1
array = np.loadtxt("Day 1/input", dtype=int)
col1, col2 = array.T
col1.sort()
col2.sort()
distances = abs(col2-col1)
print(distances.sum())

# Part 2
score = 0
for value in col1:
    score += value * (col2 == value).sum()

print(score)