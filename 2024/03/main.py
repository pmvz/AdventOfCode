import re


with open("2024/03/input") as file:
    content = file.read()


# Part 1
# Find all 'mul(number,number)' substrings and multiply the numbers
total = 0
for match in re.finditer(r"mul\((\d+?),(\d+?)\)", content):
    nums = match.groups()
    total += int(nums[0]) * int(nums[1])

print(total)


# Part 2
# 'mul(number,number)' substrings between a 'do()' and a 'don't()'
total = 0
for match in re.finditer(r"do\(\).+?don't\(\)", content, re.DOTALL):
    for submatch in re.finditer(r"mul\((\d+?),(\d+?)\)", match.group(0)):
        nums = submatch.groups()
        total += int(nums[0]) * int(nums[1])

# Also include muls before the first 'don't()'
for match in re.finditer(r"mul\((\d+?),(\d+?)\)", content[:content.find("don't()")]):
    nums = match.groups()
    total += int(nums[0]) * int(nums[1])

print(total)
