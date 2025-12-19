from collections import defaultdict


with open("2024/11/input") as file:
    numbers = list(map(int, file.read().strip().split()))


# Initialize a dictionary to keep track of stone frequencies,
# defaultdict sets not-yet-existing items to 0 when indexed
number_freqs = defaultdict(int)

for num in numbers:
    number_freqs[num] += 1

# Repeat the instructions 25 (part 1) or 75 times (part 2)
for iteration in range(75):
    new_freqs = defaultdict(int)
    for num in number_freqs:
        # 0 always becomes 1
        if num == 0:
            new_freqs[1] += number_freqs[0]
        # Numbers with an even amount of digits get split
        elif len(strnum := str(num)) % 2 == 0:
            new_freqs[int(strnum[:len(strnum)//2])] += number_freqs[num]
            new_freqs[int(strnum[len(strnum)//2:])] += number_freqs[num]
        # All other numbers get multiplied
        else:
            new_freqs[2024*num] += number_freqs[num]

    number_freqs = new_freqs

print(sum(number_freqs.values()))
