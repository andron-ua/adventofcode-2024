import re


ans = 0
data = []
p1 = re.compile(r'XMAS')
p2 = re.compile(r'SAMX')
with open('04.data') as file:
    for line in file:
        ans = ans + len(p1.findall(line))
        ans = ans + len(p2.findall(line))
        data.append(line.strip())
for row in zip(*data):
    line = ''.join(row)
    ans = ans + len(p1.findall(line))
    ans = ans + len(p2.findall(line))

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

for row in data2:
    line = ''.join(row)
    ans = ans + len(p1.findall(line))
    ans = ans + len(p2.findall(line))

for row in zip(*data2):
    line = ''.join(row)
    ans = ans + len(p1.findall(line))
    ans = ans + len(p2.findall(line))

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

for row in data2:
    line = ''.join(row)
    ans = ans + len(p1.findall(line))
    ans = ans + len(p2.findall(line))

for row in zip(*data2):
    line = ''.join(row)
    ans = ans + len(p1.findall(line))
    ans = ans + len(p2.findall(line))

print(ans)
