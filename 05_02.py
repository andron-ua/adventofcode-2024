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
                update2 = []
                seen = set(update)
                while update:
                    num = update.pop()
                    if len(rules[num] & seen):
                        update.insert(0, num)
                    else:
                        update2.insert(0, num)
                        seen.remove(num)
                ans = ans + update2[len(update2) // 2]
                break
            seen.add(num)
print(ans)
