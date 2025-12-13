import numpy as np


with open("2024/02/input") as file:
    lines = file.readlines()


def is_valid_sequence(sequence):
    """
    Returns True if the sequence is strictly increasing or 
    strictly decreasing with absolute differences no greater than 3
    """
    diffs = np.diff(sequence)
    return ((diffs > 0).all() or (diffs < 0).all()) and (abs(diffs) <= 3).all()


# Part 1
safe = 0
for line in lines:
    safe += is_valid_sequence(np.array(line.split(), dtype=int))

print(safe)


# Part 2
safe = 0
for line in lines:
    nums = np.array(line.split(), dtype=int)
    
    # Check if no problem dampener is needed
    if is_valid_sequence(nums):
        safe += 1
        continue
    
    # Find errors
    diffs = np.diff(nums)
    errors = (abs(diffs) > 3) | (abs(diffs) < 1)
    mostly_increasing = (diffs > 0).sum() > (diffs < 0).sum()
    if mostly_increasing:
        errors |= diffs <= 0
    else:
        errors |= diffs >= 0

    # Delete the number before or after the first error and check again
    indices = np.argwhere(errors).flatten()
    nums_new_before = np.delete(nums, indices[0])
    nums_new_after = np.delete(nums, indices[0]+1)

    if is_valid_sequence(nums_new_before) or is_valid_sequence(nums_new_after):
        safe += 1
        continue


print(safe)
