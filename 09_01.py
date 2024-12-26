puzzle: list[int] = []
with open('09.data') as file:
    for char in file.readline().strip():
        puzzle.append(int(char))

disk: list[int] = []
for idx, block in enumerate(puzzle):
    disk.extend([0 if idx % 2 else idx // 2] * block)

left, right = puzzle[0], len(disk) - 1
while left <= right:
    while disk[left]:
        left = left + 1
    if left >= right:
        break
    while not disk[right]:
        right = right - 1
    disk[left], disk[right] = disk[right], disk[left]

print(sum(idx * num for idx, num in enumerate(disk)))
