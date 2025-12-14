import numpy as np


def get_letter(array, loc):
    if 0 <= loc[0] < array.shape[0] and 0 <= loc[1] < array.shape[1]:
        return array[*loc]
    else:
        return "Nope"


def is_xmas_start(array, loc):
    # There is probably a numpy trick to get this array but I don't know it
    vectors = np.array([[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]])
    starts = 0
    for vector in vectors:
        # Uses lazy evaluation
        if (get_letter(array, loc) == "X" and get_letter(array, loc+vector) == "M" and
            get_letter(array, loc+2*vector) == "A" and get_letter(array, loc+3*vector) == "S"):
            starts += 1

    return starts


# Parsing
with open("2024/04/input") as file:
    content = file.read()

array = np.array([[char for char in line] for line in content.split()], dtype="<U1")


# Part 1
count = 0
for i, row in enumerate(array):
    for j, char in enumerate(row):
        count += is_xmas_start(array, np.array([i,j]))

print(count)


# Part 2
# All X-MAS must be centered on an A
count = 0
for a_idx in np.argwhere(array == "A"):
    # Get the 3x3 window around A
    window = array[a_idx[0]-1:a_idx[0]+2, a_idx[1]-1:a_idx[1]+2]
    if window.shape != (3,3):
        continue

    # Only four possible cases
    if ((window[0,0] == "M" and window[0,2] == "M" and window[2,0] == "S" and window[2,2] == "S") or
        (window[0,0] == "M" and window[0,2] == "S" and window[2,0] == "M" and window[2,2] == "S") or
        (window[0,0] == "S" and window[0,2] == "M" and window[2,0] == "S" and window[2,2] == "M") or
        (window[0,0] == "S" and window[0,2] == "S" and window[2,0] == "M" and window[2,2] == "M")):
        count += 1

print(count)
