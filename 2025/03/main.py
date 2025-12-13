with open("Day 3/input") as file:
    batteries = file.readlines()

total_joltage = 0

for battery in batteries:
    battery = battery.rstrip('\n')
    remaining_batteries = 12  # 2 for part 1, 12 for part 2
    joltage = ""

    while remaining_batteries > 0:
        remaining_batteries -= 1

        # Find the highest single value in the string that leaves enough remaining batteries
        for label in "987654321":
            i = battery.find(label)
            if i == -1 or i >= len(battery)-remaining_batteries:
                continue
            else:
                joltage += label
                break

        # Disregard all values left of the label that was chosen
        battery = battery[i+1:]

    print("The highest joltage is " + joltage)
    total_joltage += int(joltage)
    
print(f"The total joltage is {total_joltage}")
