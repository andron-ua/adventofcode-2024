puzzle :list[list[int]] = []
pos = None
with open('06.data') as file:
    for line in file:
        puzzle.append(list(line.strip()))
        if '^' in puzzle[-1]:
            pos = len(puzzle) - 1 + puzzle[-1].index('^') * 1j
            puzzle[-1][int(pos.imag)] = 'X'
boundary = len(puzzle)
dir = -1
while True:
    next_pos = pos + dir
    if int(next_pos.real) < 0 \
            or int(next_pos.real) == boundary \
            or int(next_pos.imag) < 0 \
            or int(next_pos.imag) == boundary:
        break
    if puzzle[int(next_pos.real)][int(next_pos.imag)] == '#':
        dir = dir * -1j
    else:
        puzzle[int(next_pos.real)][int(next_pos.imag)] = 'X'
        pos = next_pos

ans = 0
for _ in puzzle:
    ans = ans + _.count('X')

print(ans)
