q = [0, 0, 0, 0]
w, h, seconds = 101, 103, 100
with open('14.data') as file:
    for line in file:
        a, b = line.strip().split()
        px, py = (int(_) for _ in a[2:].split(','))
        vx, vy = (int (_) for _ in b[2:].split(','))
        px, py = (px + seconds * vx) % w, (py + seconds * vy) % h
        if px < w // 2 and py < h // 2:
            q[0] = q[0] + 1
        elif px < w // 2 and py > h // 2:
            q[1] = q[1] + 1
        elif px > w // 2 and py > h // 2:
            q[2] = q[2] + 1
        elif px > w // 2 and py < h // 2:
            q[3] = q[3] + 1
print(q[0] * q[1] * q[2] * q[3])
