from collections import Counter


ans = 0
nums1, nums2 = [], []
with open('01.data') as file:
    for pair in file:
        num1, num2 = pair.strip().split()
        nums1.append(int(num1))
        nums2.append(int(num2))
counter1 = Counter(nums1)
counter2 = Counter(nums2)
for num, cnt in counter1.items():
    ans = ans + num * cnt * counter2[num]
print(ans)
