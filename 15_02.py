warehouse: list[list[str]] = []
moves: str = ''
robot: tuple[int]
with open('15.data') as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        warehouse.append([_ for chain in zip(
            ('[' if _ == 'O' else _ for _ in line),
            (']' if _ == 'O' else _ for _ in line))
            for _ in chain])
        if '@' in warehouse[-1]:
            robot = (len(warehouse) - 1, warehouse[-1].index('@'))
            warehouse[-1][robot[1]] = '.'
            warehouse[-1][robot[1]+1] = '.'
    for _ in range(len(warehouse)):
        warehouse.append(['.'] * len(warehouse[0]))
    for line in file:
        moves = moves + line.strip()


def rotate(matrix: list[list[str]]):
    for idx in range(len(matrix) // 2):
        matrix[idx], matrix[-1 - idx] = matrix[-1 - idx], matrix[idx]
    for row in range(len(matrix)):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


prev_move = '>'
rotations = {
    '>>': 0, 'vv': 0, '<<': 0, '^^': 0,
    '>^': 1, 'v>': 1, '<v': 1, '^<': 1,
    '><': 2, 'v^': 2, '<>': 2, '^v': 2,
    '>v': 3, 'v<': 3, '<^': 3, '^>': 3,
}


def print_matrix(matrix: list[list[str]], move: str, robot: tuple[int]):
    for _ in range(rotations[move + '>']):
        robot = (robot[1], len(matrix) - 1 - robot[0])
        rotate(matrix)
    print(move)
    for row_idx, row in enumerate(matrix[:len(matrix) // 2]):
        if row_idx == robot[0]:
            row[robot[1]] = '@'
        print(''.join(row))
        if row_idx == robot[0]:
            row[robot[1]] = '.'
    for _ in range(rotations['>' + move]):
        rotate(matrix)


def move_horizontal(warehouse: list[list[str]], move: str, robot: tuple[int]) -> tuple[int]:
    line = warehouse[robot[0]]
    wall = line.index('#', robot[1])
    try:
        empty_tile = line.index('.', robot[1]+1)
        if wall > empty_tile > robot[1]:
            for idx in range(empty_tile, robot[1], -1):
                line[idx] = line[idx-1]
            line[robot[1]] = '.'
            robot = (robot[0], robot[1]+1)
    except ValueError:
        pass
    return robot


def find_pair(warehouse: list[list[str]], move: str, robot: tuple[int]) -> tuple[int]:
    curr_tile = warehouse[robot[0]][robot[1]]
    if move == '^':
        if curr_tile == '[':
            paired_tile = (robot[0] + 1, robot[1])
        else:
            paired_tile = (robot[0] - 1, robot[1])
    else:
        if curr_tile == '[':
            paired_tile = (robot[0] - 1, robot[1])
        else:
            paired_tile = (robot[0] + 1, robot[1])
    return paired_tile


def try_move(warehouse: list[list[str]], move: str, robot: tuple[int], move_pair: bool = True) -> bool:
    next_tile = warehouse[robot[0]][robot[1]+1]
    if move_pair:
        paired_robot = find_pair(warehouse, move, robot)
        tile = warehouse[robot[0]][robot[1]]
        paired_tile = warehouse[paired_robot[0]][paired_robot[1]]
        next_paired_tile = warehouse[paired_robot[0]][paired_robot[1]+1]
        if tile == next_tile and paired_tile == next_paired_tile:
            return try_move(warehouse, move, (robot[0], robot[1] + 1))
        if '#' in (next_tile, next_paired_tile):
            return False
        if next_tile == next_paired_tile == '.':
            return True
        return (next_tile == '.' or try_move(warehouse, move, (robot[0], robot[1] + 1))) and \
            (next_paired_tile == '.' or try_move(warehouse, move, (paired_robot[0], paired_robot[1] + 1)))
    if next_tile == '#':
        return False
    elif next_tile == '.':
        return True
    else:
        return try_move(warehouse, move, (robot[0], robot[1] + 1))


def swap_tiles(warehouse: list[list[str]], tile1: tuple[int], tile2: tuple[int]):
    warehouse[tile1[0]][tile1[1]], warehouse[tile1[0]][tile1[1] + 1] = \
        warehouse[tile1[0]][tile1[1] + 1], warehouse[tile1[0]][tile1[1]]
    warehouse[tile2[0]][tile2[1]], warehouse[tile2[0]][tile2[1] + 1] = \
        warehouse[tile2[0]][tile2[1] + 1], warehouse[tile2[0]][tile2[1]]


def do_move(warehouse: list[list[str]], move: str, robot: tuple[int], move_pair: bool = True) -> tuple[int]:
    next_tile = warehouse[robot[0]][robot[1]+1]
    if move_pair:
        paired_robot = find_pair(warehouse, move, robot)
        tile = warehouse[robot[0]][robot[1]]
        paired_tile = warehouse[paired_robot[0]][paired_robot[1]]
        next_paired_tile = warehouse[paired_robot[0]][paired_robot[1]+1]
        if tile == next_tile and paired_tile == next_paired_tile:
            do_move(warehouse, move, (robot[0], robot[1] + 1))
            swap_tiles(warehouse, robot, paired_robot)
            return (0, 0)
        if '#' in (next_tile, next_paired_tile):
            return (0, 0)
        if next_tile == next_paired_tile == '.':
            swap_tiles(warehouse, robot, paired_robot)
            return (0, 0)
        if next_tile != '.':
            do_move(warehouse, move, (robot[0], robot[1] + 1))
        if next_paired_tile != '.':
            do_move(warehouse, move, (paired_robot[0], paired_robot[1] + 1))
        if next_tile != '.' or next_paired_tile != '.':
            swap_tiles(warehouse, robot, paired_robot)
        return (0, 0)
    elif next_tile == '.':
        return (robot[0], robot[1] + 1)
    else:
        do_move(warehouse, move, (robot[0], robot[1] + 1))
        return (robot[0], robot[1] + 1)


def move_vertical(warehouse: list[list[str]], move: str, robot: tuple[int]) -> tuple[int]:
    if try_move(warehouse, move, robot, False):
        return do_move(warehouse, move, robot, False)
    return robot


movers = {
    '>': move_horizontal,
    '<': move_horizontal,
    '^': move_vertical,
    'v': move_vertical,
}

for move in moves:
    for _ in range(rotations[prev_move + move]):
        robot = (robot[1], len(warehouse) - 1 - robot[0])
        rotate(warehouse)

    robot = movers[move](warehouse, move, robot)

    prev_move = move

for _ in range(rotations[prev_move + '>']):
    robot = (robot[1], len(warehouse) - 1 - robot[0])
    rotate(warehouse)

ans = 0
for row_idx, row in enumerate(warehouse):
    for col_idx, tile in enumerate(row):
        if tile == '[':
            ans = ans + 100 * row_idx + col_idx
print(ans)
