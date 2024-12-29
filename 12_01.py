from itertools import product


puzzle: list[list[int]] = []
with open('12.data') as file:
    for row, line in enumerate(file.readlines()):
        puzzle.append(list(line.strip()))

boundary = len(puzzle)
seen: set[tuple[int, int]] = set()


def discover_region(region: set[tuple[int, int]], pos: tuple[int, int]) -> None:
    if pos in seen:
        return
    seen.add(pos)
    region.add(pos)
    for next_pos in ((pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                     (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)):
        if next_pos[0] < 0 or next_pos[0] == boundary \
                or next_pos[1] < 0 or next_pos[1] == boundary \
                or puzzle[pos[0]][pos[1]] != puzzle[next_pos[0]][next_pos[1]]:
            continue
        discover_region(region, next_pos)


price = 0
for pos in product(range(boundary), range(boundary)):
    region = set()
    discover_region(region, pos)
    area, perimeter = len(region), 0
    while region:
        plot = region.pop()
        perimeter = perimeter + 4
        for next_plot in ((plot[0] + 1, plot[1]), (plot[0] - 1, plot[1]),
                          (plot[0], plot[1] + 1), (plot[0], plot[1] - 1)):
            if next_plot in region:
                perimeter = perimeter - 2
    price = price + area * perimeter
print(price)
