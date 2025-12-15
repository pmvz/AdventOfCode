import numpy as np
from numba import njit


# I should have figured delimiter=1 out earlier
array = np.genfromtxt("2024/06/input", dtype="<U1", delimiter=1, comments=" ")
rotationmatrix = np.array([[0, -1], [1, 0]])

# Find the starting point and direction, and define a matrix to track visited tiles
visited = np.full_like(array, False, dtype=bool)
position = np.argwhere(array == "^")[0]
direction = np.array([-1, 0])


@njit(cache=True)
def exits_map(array, position, direction, visited):
    """
    Returns the amount of visited tiles if the guard exits
    in less than 10000 steps, or -1 if it does not exit
    """
    steps = 0
    while steps < 5000:
        # Find the next tile and check if it is in bounds
        nextpos = position + direction
        if not 0 <= nextpos[0] < array.shape[0] or not 0 <= nextpos[1] < array.shape[1]:
            return visited.sum()

        # Rotate the direction vector if the next tile is blocked
        while array[nextpos[0], nextpos[1]] == "#":
            direction = np.array([direction[1], -direction[0]], dtype=np.int32)
            nextpos = position + direction
        
        # Update the position and add to tracked tiles
        position = nextpos
        visited[position[0], position[1]] = True

        steps += 1
    else:
        return -1


# Part 1
print(exits_map(array, position.copy(), direction.copy(), visited) + 1)

# Part 2: semi-brute force
@njit(cache=True)
def count_loops(array, position, direction, visited):
    """
    Place an obstacle at each visited tile and check if the guard still exits
    """
    loops = 0
    for obstacle_position in np.argwhere(visited):
        array[obstacle_position[0], obstacle_position[1]] = "#"
        
        if exits_map(array, position.copy(), direction.copy(), visited) == -1:
            loops += 1

        array[obstacle_position[0], obstacle_position[1]] = "."

    return loops


print(count_loops(array, position, direction, visited))
