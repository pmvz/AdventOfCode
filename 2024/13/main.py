import numpy as np
import re


parser = re.compile(r"(\d+).+?(\d+).+?(\d+).+?(\d+).+?(\d+).+?(\d+)", re.DOTALL)

with open("2024/13/input") as file:
    machines = file.read().split("\n\n")


cost = np.array([3, 1])  # Token cost per button press (3 for A, 1 for B)
total_cost_part1 = total_cost_part2 = 0

for machine in machines:
    # Parse the input by extracting all numbers as integers
    captures = parser.search(machine)
    ax, ay, bx, by, gx, gy = map(int, captures.groups())
    
    # Write the coordinate steps as a matrix
    steps = np.array([[ax, bx], [ay, by]])
    
    # Solve the amount of presses for the original goal
    # Originally used scipy.optimize.linprog but that didn't work for part 2
    goal = np.array([gx, gy])
    solution = np.rint(np.linalg.solve(steps, goal))
    if (steps @ solution == goal).all():
        total_cost_part1 += cost.T @ solution

    # Resolve for the shifted goal
    goal = np.array([gx, gy]) + 10000000000000
    solution = np.rint(np.linalg.solve(steps, goal))
    if (steps @ solution == goal).all():
        total_cost_part2 += cost.T @ solution


print(total_cost_part1, total_cost_part2)
