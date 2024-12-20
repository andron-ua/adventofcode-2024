import re


ans = 0
with open('03.data') as file:
    for line in file:
        for num1, num2 in re.compile(r'mul\((\d{1,3}),(\d{1,3})\)').findall(line):
            ans = ans + int(num1) * int(num2)
print(ans)
