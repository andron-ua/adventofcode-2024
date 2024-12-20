import re


ans = 0
enabled = True
with open('03.data') as file:
    for line in file:
        for match in re.compile(r'(do)\(\)|(don)\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)').findall(line):
            if match[0]:
                enabled = True
            elif match[1]:
                enabled = False
            elif enabled:
                ans = ans + int(match[2]) * int(match[3])
print(ans)
