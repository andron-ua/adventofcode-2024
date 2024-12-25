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
        antinode = (b[0] + delta[0], b[1] + delta[1])
        if 0 <= antinode[0] < boundary and 0 <= antinode[1] < boundary:
            antinodes.add(antinode)
        antinode = (a[0] - delta[0], a[1] - delta[1])
        if 0 <= antinode[0] < boundary and 0 <= antinode[1] < boundary:
            antinodes.add(antinode)

print(len(antinodes))
