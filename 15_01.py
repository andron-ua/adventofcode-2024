warehouse: list[list[str]] = []
moves: str = ''
robot: tuple[int]
with open('15.data') as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        warehouse.append(list(line))
        if '@' in warehouse[-1]:
            robot = (len(warehouse) - 1, warehouse[-1].index('@'))
            warehouse[-1][robot[1]] = '.'
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
    for row_idx, row in enumerate(matrix):
        if row_idx == robot[0]:
            row[robot[1]] = '@'
        print(''.join(row))
        if row_idx == robot[0]:
            row[robot[1]] = '.'
    for _ in range(rotations['>' + move]):
        rotate(matrix)


# print_matrix(warehouse, '>', robot)
for move in moves:
    # print_matrix(warehouse)
    for _ in range(rotations[prev_move + move]):
        robot = (robot[1], len(warehouse) - 1 - robot[0])
        rotate(warehouse)

    line = warehouse[robot[0]]
    # print(line)
    # print(move, robot)
    wall = line.index('#', robot[1])
    try:
        empty_tile = line.index('.', robot[1]+1)
        # print(robot[1], empty_tile, wall)
        if wall > empty_tile > robot[1]:
            line[robot[1]+1], line[empty_tile] = line[empty_tile], line[robot[1]+1]
            robot = (robot[0], robot[1]+1)
        # print('-->', robot)
        # print(wall, empty_tile)
    except ValueError:
        pass
    # print(line)
    # print_matrix(warehouse, move, robot)
    # input()

    prev_move = move

for _ in range(rotations[prev_move + '>']):
    robot = (robot[1], len(warehouse) - 1 - robot[0])
    rotate(warehouse)
# print_matrix(warehouse, '>', robot)

ans = 0
for row_idx, row in enumerate(warehouse):
    for col_idx, tile in enumerate(row):
        if tile == 'O':
            ans = ans + 100 * row_idx + col_idx
print(ans)