puzzle: list[list[int]] = []
w, h, seconds = 101, 103, 0
with open('14.data') as file:
    for line in file:
        a, b = line.strip().split()
        px, py = (int(_) for _ in a[2:].split(','))
        vx, vy = (int(_) for _ in b[2:].split(','))
        puzzle.append([px, py, vx, vy])

while True:
    seconds = seconds + 1
    picture = [[0] * w for _ in range(h)]
    for idx in range(len(puzzle)):
        px, py, vx, vy = puzzle[idx]
        px = puzzle[idx][0] = (px + vx) % w
        py = puzzle[idx][1] = (py + vy) % h
        picture[py][px] = picture[py][px] + 1
    for line in picture:
        max_cnt, cnt = 0, 1
        for idx in range(1, len(line)):
            if line[idx - 1] and line[idx]:
                cnt = cnt + 1
            else:
                max_cnt, cnt = max(max_cnt, cnt), 1
        if max_cnt >= 30:
            for row in picture:
                print(''.join(('X' if _ else '.') for _ in row))

            print(seconds)
            exit()
