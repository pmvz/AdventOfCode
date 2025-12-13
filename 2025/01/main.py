with open("Day 1/input") as file:
    instructions = file.readlines()

position = 50
at_zero = 0
past_zero = 0

for instruction in instructions:
    direction, rotation = instruction[0], int(instruction[1:])
    
    # Apply the rotation, inline conditional for fun
    origin = position
    position += rotation if direction == 'R' else -rotation

    # Count times past 0 and keep the position in [0,100)
    past_zero += abs(position // 100)
    position %= 100

    at_zero += position == 0

    # Avoid double-counting when starting at 0 and not counting
    # when stopping at 0 when rotating left
    if direction == 'L':
        past_zero += position == 0
        past_zero -= origin == 0

    
print(at_zero)
print(past_zero)
