import numpy as np


with open("Day 12/input") as file:
    content = file.read()

split = content.rfind("\n\n")
presents_raw = content[:split].split("\n\n")
trees_raw = content[split+2:].strip().split("\n")

presents = np.full((len(presents_raw), 3, 3), False)
for i, present in enumerate(presents_raw):
    presents[i] = np.array([[True if char == '#' else False for char in line.strip()]
                             for line in present.split()[1:]])

possible_upperbound = 0
for tree in trees_raw:
    shape, counts = tree.split(':')
    size = np.prod(shape.split('x'), dtype=int)

    size_required = 0
    for i, count in enumerate(counts.split()):
        size_required += int(count) * presents[i].sum()

    if size_required <= size:
        possible_upperbound += 1

print(possible_upperbound)