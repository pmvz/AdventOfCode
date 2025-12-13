import numpy as np


with open("Day 2/input") as file:
    lines = file.readlines()

# Part 1
safe = 0
for line in lines:
    diffs = np.diff(np.array(line.split(), dtype=int))
    # all decreasing or increasing, and all 1 <= diff <= 3
    safe += ((diffs > 0).all() or (diffs < 0).all()) and \
            ((1 <= abs(diffs)) & (abs(diffs) <= 3)).all()

print(safe)


# Part 2
safe = 0
for line in lines:
    diffs = np.diff(np.array(line.split(), dtype=int))
    
    # Check if no problem dampener is needed
    is_safe = ((diffs > 0).all() or (diffs < 0).all()) and \
              ((1 <= abs(diffs)) & (abs(diffs) <= 3)).all()
    
    if is_safe:
        safe += 1
        continue

    # Check errors in the diff range
    errors = (abs(diffs) > 3) | (abs(diffs) < 1)

    # Check errors in increase/decrease
    #np.argmin([(diffs >= 0).sum(), ])

    if (diffs >= 0).sum() >= 1 and (diffs >= 0).sum() < diffs.size-1:
        errors |= diffs >= 0
    elif (diffs <= 0).sum() >= 1 and (diffs <= 0).sum() < diffs.size-1:
        errors |= diffs <= 0

    if errors.sum() > 1:
        continue
    
    diffs = np.delete(diffs, np.argwhere(errors).flatten())
    
    # Check again
    is_safe = ((diffs > 0).all() or (diffs < 0).all()) and \
              ((1 <= abs(diffs)) & (abs(diffs) <= 3)).all()
    
    if is_safe:
        safe += 1

print(safe)  # lower than 611, higher than 514, lower than 551
