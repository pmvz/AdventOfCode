import numpy as np
from scipy.signal import convolve2d


with open("Day 4/input") as file:
    lines = file.readlines()

# Create an array of the map, and a boolean array of paper locations
array = np.array([[char for char in line if char != '\n'] for line in lines])
paper = array == '@'
previous_paper = np.full(paper.shape, True)  # Initialize as a map full of paper

# Iterate until no paper rolls are removed
total_removed = 0
while (paper != previous_paper).any():
    # Number of adjacent paper rolls for each tile
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    adjacentpaper = convolve2d(paper, kernel, mode="same")

    # Find which paper rolls have < 4 neighbouring rolls
    accessible = adjacentpaper < 4 * paper
    total_removed += accessible.sum()

    # Update the map
    previous_paper = paper.copy()
    paper ^= accessible

print(total_removed)
