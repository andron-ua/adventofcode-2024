ans = 0


def is_valid(report: list[int]) -> int:
    prev, delta, direction = 0, 0, 0
    for idx, num in enumerate(report):
        if not idx:
            prev = num
            continue
        elif idx == 1:
            delta = num - prev
            if not delta:
                return 0
            direction = -1 if delta < 0 else 1
        delta = num - prev
        if not delta:
            return 0
        curr_direction = -1 if delta < 0 else 1
        if curr_direction != direction:
            return 0
        if abs(delta) > 3:
            return 0
        prev = num
    return 1


with open('02.data') as file:
    for report in file:
        report = [int(_) for _ in report.strip().split()]
        for idx in range(len(report)):
            report2 = report.copy()
            report2.pop(idx)
            if is_valid(report2):
                ans = ans + 1
                break
print(ans)