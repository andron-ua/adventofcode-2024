puzzle: list[list[str]] = []
pos = None
with open('06.data') as file:
    for line in file:
        puzzle.append(list(line.strip()))
        if '^' in puzzle[-1]:
            pos = len(puzzle) - 1 + puzzle[-1].index('^') * 1j
            puzzle[-1][int(pos.imag)] = 'X'
boundary = len(puzzle)


def check_loop(pos: complex) -> int:
    seen = set()
    dir = -1
    while True:
        if (dir, pos) in seen:
            return 1
        seen.add((dir, pos))
        next_pos = pos + dir
        if int(next_pos.real) < 0 \
                or int(next_pos.real) == boundary \
                or int(next_pos.imag) < 0 \
                or int(next_pos.imag) == boundary:
            return 0
        if puzzle[int(next_pos.real)][int(next_pos.imag)] == '#':
            dir = dir * -1j
        else:
            pos = next_pos


ans = 0
for row in range(boundary):
    for col in range(boundary):
        if row == int(pos.real) and col == int(pos.imag):
            continue
        if puzzle[row][col] != '#':
            puzzle[row][col] = '#'
            ans = ans + check_loop(pos)
            puzzle[row][col] = '.'
print(ans)
