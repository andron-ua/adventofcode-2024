ans = 0
data = []
p = ('MAS', 'SAM')
with open('04.data') as file:
    for line in file:
        data.append(line.strip())

l = len(data[0])
data2 = [['.'] * l for _ in range(l)]
offset = l // 2 - 1
row2 = 0
for row in range(0, l * 2, 2):
    if row2 < l // 2:
        col2 = offset - row2
    else:
        col2 = row2 - offset - 1
    for col in range(row + 1):
        if row - col < l and col < l:
            data2[row2][col2] = data[row-col][col]
            col2 = col2 + 1
    row2 = row2 + 1

for row in range(1, len(data2) - 1):
    for col in range(1, len(data2[row]) - 1):
        hrz = data2[row][col-1] + data2[row][col] + data2[row][col+1]
        vrt = data2[row-1][col] + data2[row][col] + data2[row+1][col]
        if hrz in p and vrt in p:
            ans = ans + 1

data2 = [['.'] * l for _ in range(l)]
offset = l // 2 - 1
row2 = 0
for row in range(1, l * 2, 2):
    if row2 < l // 2:
        col2 = offset - row2
    else:
        col2 = row2 - offset
    for col in range(row + 1):
        if row - col < l and col < l:
            data2[row2][col2] = data[row-col][col]
            col2 = col2 + 1
    row2 = row2 + 1

for row in range(1, len(data2) - 1):
    for col in range(1, len(data2[row]) - 1):
        hrz = data2[row][col-1] + data2[row][col] + data2[row][col+1]
        vrt = data2[row-1][col] + data2[row][col] + data2[row+1][col]
        if hrz in p and vrt in p:
            ans = ans + 1

print(ans)
