from heapq import heappush, heappop


def complex2tuple(c: complex) -> tuple[int, int]:
    return (int(c.real), int(c.imag))


def tuple2complex(t: tuple[int, int]) -> complex:
    return complex(*t)


maze: list[list[str]] = []
q: list[tuple] = []
score: int = 0
pos: int
dir: complex = 1j
visited: set[tuple] = set()
with open('16.data') as file:
    for line in file:
        line = line.strip()
        maze.append(list(line))
        if 'S' in maze[-1]:
            pos = len(maze) - 1 + maze[-1].index('S') * 1j
            q.append((score, complex2tuple(pos), complex2tuple(dir)))
            visited.add((pos, dir))
            q.append((score + 1000, complex2tuple(pos), complex2tuple(dir * 1j)))
            visited.add((pos, dir))
            q.append((score + 1000, complex2tuple(pos),
                     complex2tuple(dir * (-1j))))
            visited.add((pos, dir))
            q.append((score + 2000, complex2tuple(pos), complex2tuple(-dir)))
            visited.add((pos, dir))

while q:
    score, pos, dir = heappop(q)
    pos = tuple2complex(pos)
    dir = tuple2complex(dir)
    next_pos = pos + dir
    next_score = score + 1
    tile = maze[int(next_pos.real)][int(next_pos.imag)]
    if tile == 'E':
        print(next_score)
        break
    if tile == '#' or (next_pos, dir) in visited:
        continue
    heappush(q, (next_score, complex2tuple(next_pos), complex2tuple(dir)))
    visited.add((next_pos, dir))

    # counterclockwise
    next_dir = dir * 1j
    if (next_pos, next_dir) not in visited:
        heappush(q, (next_score + 1000, complex2tuple(next_pos),
                 complex2tuple(next_dir)))
        visited.add((next_pos, next_dir))

    # clockwise
    next_dir = dir * (-1j)
    if (next_pos, next_dir) not in visited:
        heappush(q, (next_score + 1000, complex2tuple(next_pos),
                 complex2tuple(next_dir)))
        visited.add((next_pos, next_dir))
