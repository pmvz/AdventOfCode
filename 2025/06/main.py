import numpy as np


# Part 1
array = np.loadtxt("Day 6/input", dtype=str)
instructions = array[-1]
values = array[:-1].astype(np.uint64)

products = np.prod(values, axis=0)
sums = np.sum(values, axis=0)

print(np.sum(products[instructions == '*']) + np.sum(sums[instructions == '+']))


# Part 2
with open("Day 6/input") as file:
    lines = file.readlines()

# Load the values as arrays of characters, including spaces
instructions = None
chars = []
for line in lines:
    if line[0] in "*+":
        instructions = np.array(line.split())
    else:
        chars.append(np.array([char for char in line if char != '\n']))

# Find where all rows have a space, indicating a next block of numbers, and split there
chars = np.array(chars)
spaces = chars == ' '
splits = np.where(spaces.all(axis=0))[0]  
chars_split = np.split(chars, splits, axis=1)

# Process each block
total = 0
for instruction, chars_block in zip(instructions, chars_split):
    values = [int(''.join(row)) for row in chars_block.T if (row != ' ').any()]
    if instruction == '*':
        total += np.prod(values, dtype=np.uint64)
    elif instruction == '+':
        total += np.sum(values, dtype=np.uint64)

print(total)
