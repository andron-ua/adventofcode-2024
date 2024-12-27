puzzle: list[list[int]] = []
trailheads: list[tuple[int, int]] = []
with open('10.data') as file:
    for row, line in enumerate(file.readlines()):
        puzzle.append([int(_) for _ in line.strip()])
        for col, height in enumerate(puzzle[row]):
            if height == 0:
                trailheads.append((row, col))


boundary = len(puzzle)
seen: set[tuple[int, int]] = set()
seen9: set[tuple[int, int]] = set()


def find_path(height: int, pos: tuple[int, int]) -> int:
    if pos[0] < 0 or pos[0] == boundary \
            or pos[1] < 0 or pos[1] == boundary:
        return 0
    if pos in seen or pos in seen9:
        return 0
    if puzzle[pos[0]][pos[1]] != height:
        return 0
    if puzzle[pos[0]][pos[1]] == 9:
        seen9.add(pos)
        return 1
    seen.add(pos)
    ret = find_path(height + 1, (pos[0] + 1, pos[1])) \
        + find_path(height + 1, (pos[0] - 1, pos[1])) \
        + find_path(height + 1, (pos[0], pos[1] + 1)) \
        + find_path(height + 1, (pos[0], pos[1] - 1))
    seen.remove(pos)

    return ret


ans = 0
for row, col in trailheads:
    seen, seen9 = set(), set()
    ans = ans + find_path(0, (row, col))

print(ans)
