from collections import namedtuple


with open("2024/09/input") as file:
    diskmap = file.read().strip()


current_ID = 0
disk = []

# Build disk
for i in range(len(diskmap)):
    if i % 2 == 0:
        for _ in range(int(diskmap[i])):
            disk.append(int(current_ID))
        current_ID += 1

    else:        
        for _ in range(int(diskmap[i])):
            disk.append(-1)

# Compress (part 1)
for i in range(len(disk)):
    try:
        if disk[i] == -1:
            while (newvalue := disk.pop()) == -1:
                pass
            disk[i] = newvalue
    except IndexError:
        disk.append(newvalue)
        break

# Checksum
print(sum(i*value for i, value in enumerate(disk)))


# Build disk again, but with named tuples
Item = namedtuple("Item", ["size", "is_file", "id"], defaults=[False, 0, -1])

disk = []
diskmap += "0"  # Make len(diskmap) even for easier unpacking
for file_id in range(len(diskmap) // 2):
    file_size, space_size = diskmap[2*file_id:2*file_id+2]
    disk.append(Item(int(file_size), True, file_id))
    disk.append(Item(int(space_size)))

disk.pop()  # Remove the added 0

# Compress (part 2): iterate over all files
index_read = len(disk) - 1
for file_id in range(disk[-1].id, -1, -1):
    while (item_r := disk[index_read]).id != file_id:
        index_read -= 1

    # Find the leftmost space the file fits in and is left of the file,
    # then place the file there and make the original item a space
    for index_write in range(index_read):
        if index_write >= index_read:
            break

        item_w = disk[index_write]
        if not item_w.is_file and item_w.size >= item_r.size:
            disk[index_read] = Item(item_r.size)
            disk.insert(index_write, item_r)
            disk[index_write+1] = item_w._replace(size=item_w.size-item_r.size)
            break


# Calculate the checksum
checksum = 0
index = 0
for item in disk:
    i = item.size
    while i > 0:
        if item.is_file:
            checksum += index * item.id
        index += 1
        i -= 1

print(checksum)
