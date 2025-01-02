puzzle: list[dict] = []
with open('13.data') as file:
    while True:
        machine = {}
        a, b = file.readline().strip().split()[-2:]
        machine['a'] = (int(a[2:-1]), int(b[2:]))
        a, b = file.readline().strip().split()[-2:]
        machine['b'] = (int(a[2:-1]), int(b[2:]))
        a, b = file.readline().strip().split()[-2:]
        machine['p'] = (10000000000000 + int(a[2:-1]), 10000000000000 + int(b[2:]))
        puzzle.append(machine)
        if not file.readline():
            break

answer = 0
for machine in puzzle:
    a, b, p = machine['a'], machine['b'], machine['p']
    count_b = (p[0] * a[1] - p[1] * a[0]) / (b[0] * a[1] - b[1] * a[0])
    count_a = (p[1] - count_b * b[1]) / a[1]

    if count_a == int(count_a) and count_b == int(count_b):
        answer = answer + int(count_a) * 3 + int(count_b)

print(answer)
