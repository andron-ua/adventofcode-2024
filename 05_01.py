from collections import defaultdict


rules = defaultdict(set)
ans = 0
with open('05.data') as file:
    while line := file.readline().strip():
        a, b = line.split('|')
        rules[int(a)].add(int(b))
    while line := file.readline().strip():
        update = [int(_) for _ in line.split(',')]
        seen = set()
        for num in update:
            if rules[num] & seen:
                break
            seen.add(num)
        else:
            ans = ans + update[len(update) // 2]
print(ans)
