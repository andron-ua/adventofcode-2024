from collections import defaultdict
from itertools import combinations


puzzle = defaultdict(list)
boundary = 0
with open('08.data') as file:
    for row, line in enumerate(file):
        boundary = boundary + 1
        for col, antenna in enumerate(line.strip()):
            if antenna == '.':
                continue
            puzzle[antenna].append((row, col))

antinodes = set()
for antennas in puzzle.values():
    for a, b in combinations(antennas, r=2):
        delta = (b[0] - a[0], b[1] - a[1])
        antinode = b
        while True:
            if not (0 <= antinode[0] < boundary and 0 <= antinode[1] < boundary):
                break
            antinodes.add(antinode)
            antinode = (antinode[0] + delta[0], antinode[1] + delta[1])
        antinode = a
        while True:
            if not (0 <= antinode[0] < boundary and 0 <= antinode[1] < boundary):
                break
            antinodes.add(antinode)
            antinode = (antinode[0] - delta[0], antinode[1] - delta[1])

print(len(antinodes))
