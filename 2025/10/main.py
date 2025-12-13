import numpy as np
import re
from itertools import combinations
from scipy.optimize import linprog


with open("Day 10/input") as file:
    machines = file.readlines()


# Part 1
total_presses = 0
for machine in machines:
    solution_found = False

    # Get the desired indicator lights and initialize an array for the current state
    desired_state = machine[1:machine.find(']')]
    desired_state = np.array([True if char == '#' else False for char in desired_state])
    current_state = np.full_like(desired_state, False)
    
    # Get all button configurations
    buttons = re.findall(r"\(([\d,]+)\)", machine)
    buttons = [[int(toggle) for toggle in button.split(',')] for button in buttons]

    # Technically a breadth-first search without caching, I think
    for i in range(1, len(buttons)):
        for combination in combinations(buttons, i):
            current_state[:] = False
            for button in combination:
                current_state[button] = ~current_state[button]

            if (current_state == desired_state).all():
                total_presses += i
                solution_found = True
                break
        
        if (solution_found):
            break

print(total_presses)


# Part 2
total_presses = 0
for machine in machines:
    # Get all button configurations (again) and minimum joltage
    buttons = re.findall(r"([\d,]+)", machine)
    joltage = buttons.pop()
    buttons = [[int(toggle) for toggle in button.split(',')] for button in buttons]
    joltage = [int(jolt) for jolt in joltage.split(',')]

    # Construct the matrix for which buttons increments which joltage
    matrix = np.zeros((len(joltage), len(buttons)))
    for row, button in zip(matrix.T, buttons):
        row[button] = 1  # Button is a list, this sets the element to 1 for each index

    # Let scipy solve the linear algebra
    result = linprog(np.ones(len(buttons)), A_eq=matrix, b_eq=joltage, integrality=1)
    total_presses += int(result.fun)

print(total_presses)
