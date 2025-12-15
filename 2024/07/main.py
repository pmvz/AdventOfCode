from collections import deque
from itertools import product, chain


with open("2024/07/input") as file:
    lines = file.readlines()


total_valid = 0
for line in lines:
    result, nums = line.strip().split(":")
    result = int(result)
    nums = list(map(int, nums.split()))
    
    # Iterate over all operator permutations (_ is used for || in part 2, remove
    # it for part 1). Part 2 takes 2 min, functools.cache does not speed this up
    for operators in list(product("*+_", repeat=len(nums)-1)):
        calculation = deque(chain.from_iterable(zip(nums, operators)))
        calculation.append(nums[-1])
        current_result = calculation.popleft()

        # Evaluate the expression
        while len(calculation) >= 2:
            operator = calculation.popleft()
            if operator == "*":
                current_result *= calculation.popleft()
            elif operator == "_":
                current_result = int(str(current_result) + str(calculation.popleft()))
            else:  # +
                current_result += calculation.popleft()

            # Stop evaluating if the current result is already higher than result
            if current_result > result:
                continue

        if current_result == result:
            total_valid += result
            break

print(total_valid)
