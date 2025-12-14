with open("2024/05/input") as file:
    content = file.read()

rules, updates = content.split("\n\n")
rules = {tuple(rule.split("|")) for rule in rules.split()}


def is_correct(nums, rules):
    "Check if the ordering is correct for each number pair"
    for i in range(len(nums)-1):
        if (nums[i], nums[i+1]) not in rules:
            return False
        
    return True


# Part 1
incorrect_updates = []
middle_sum = 0
for update in updates.split():
    nums = update.split(",")

    # Store incorrect sequences and continue with the next one
    if not is_correct(nums, rules):
        incorrect_updates.append(nums)
        continue

    middle_sum += int(nums[len(nums)//2])

print(middle_sum)


# Part 2
# Some sort of sorting algorithm, probably inefficient bubble sort or something
middle_sum = 0
for nums in incorrect_updates:
    for _ in range(len(nums)):
        # Swap values that appear in reverse order in the rules
        for i in range(len(nums)-1):
            if (nums[i+1], nums[i]) in rules:
                nums[i+1], nums[i] = nums[i], nums[i+1]

        if is_correct(nums, rules):
            middle_sum += int(nums[len(nums)//2])
            break

print(middle_sum)
