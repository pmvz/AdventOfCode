filename = r"Day 1\input"
position = 50
zeroes = 0

with open(filename) as file:
    instructions = file.readlines()

for instruction in instructions:
    rotation = int(instruction[1:])
    
    if instruction[0] == 'L':
        rotation *= -1

    # ran into some issues with mod :)
    while rotation != 0:
        if rotation < 0:
            position -= 1
            rotation += 1
        else:
            position += 1
            rotation -= 1

        position %= 100
        if position == 0:
            zeroes += 1
    
print(zeroes)
