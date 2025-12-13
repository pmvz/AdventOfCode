# Solution for part 1 only
with open("Day 2/input") as file:
    full_ranges = file.read().rstrip('\n').split(',')

# Ranges where each range stays in the same order of magnitude
oom_ranges = []

# Split full ranges into OoM ranges. Works as long as there is at most one OoM difference
for full_range in full_ranges:
    start, stop = full_range.split('-')
    if len(start) == len(stop):
        oom_ranges.append((start, stop))
    else:
        oom_ranges.append((start, '9'*len(start)))
        oom_ranges.append(('1'+'0'*len(start), stop))
    

invalid_ids = []
for oom_range in oom_ranges:
    # Disregard odd length ranges
    start, stop = oom_range
    oom = len(start)
    if oom % 2 == 1:
        continue

    # Iterate over half-IDs
    start_half = start[:oom//2]
    stop_half = stop[:oom//2]

    invalid_ids_range = []
    for half in range(int(start_half), int(stop_half)+1):
        # Construct the full id
        invalid_id = half*10**(oom//2) + half
        
        # Check if the id is in the range
        if invalid_id in range(int(start), int(stop)+1):
            invalid_ids.append(invalid_id)
            invalid_ids_range.append(invalid_id)


print(sum(invalid_ids))
