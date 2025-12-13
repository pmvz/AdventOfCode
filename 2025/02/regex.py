# Solution for both part 1 and 2
import re

with open("Day 2/input") as file:
    full_ranges = file.read().rstrip('\n').split(',')

# Matches all strings that consist of repeating groups only
pattern = re.compile(r"^(.+)\1+$")

# Check every single ID to see whether it matches
invalid_IDs = []
for full_range in full_ranges:
    start, stop = full_range.split('-')
    for ID in range(int(start), int(stop)+1):
        if pattern.match(str(ID)):
            invalid_IDs.append(ID)

print(sum(invalid_IDs))
