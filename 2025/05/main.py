# Part 1
with open("Day 5/input") as file:
    lines = file.readlines()

# Split input into ingredient IDs and ranges
split = lines.index('\n')
ID_ranges, IDs = lines[:split], lines[split+1:]

# Construct range objects from ranges
for i, ID_range in enumerate(ID_ranges):
    rmin, rmax = ID_range.split('-')
    ID_ranges[i] = range(int(rmin), int(rmax)+1)
    
# Check for each ID if it is in any range
count_fresh = 0
for ID in IDs:
    for ID_range in ID_ranges:
        if int(ID) in ID_range:
            count_fresh += 1
            break

print(count_fresh)


# Part 2
ID_ranges = lines[:split]
ID_minmaxs = []

# Instead of range objects, use tuples with a minimum and maximum
for ID_range in ID_ranges:
    rmin, rmax = ID_range.split('-')
    ID_minmaxs.append((int(rmin), int(rmax)))

# Sort the tuples from low to high
ID_minmaxs.sort()

# For each pair:
#     Check if the maximum is in the next range
#     If true, check if the maximum of that range in the next range, etc
#     The final range that contains the previous maximum has the absolute maximum, the original range the minimum
#     Continue after the final range, skip in betweens

ID_minmaxs_merged = []

for i, (mini, maxi) in enumerate(ID_minmaxs):
    min_merged = mini
    max_merged = maxi

    if len(ID_minmaxs_merged) > 0 and max_merged <= ID_minmaxs_merged[-1][1]:
        continue
    
    for j, (minj, maxj) in enumerate(ID_minmaxs[i:]):
        if minj-1 <= max_merged <= maxj:
            max_merged = maxj
        elif minj > max_merged:
            break

    ID_minmaxs_merged.append((min_merged, max_merged))


# Sum all ranges, adding one to each to include the endpoint
total = 0
for r in ID_minmaxs_merged:
    total += r[1] - r[0] + 1

print(total)
