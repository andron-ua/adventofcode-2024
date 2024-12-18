ans = 0
nums1, nums2 = [], []
with open('01.data') as file:
    for pair in file:
        num1, num2 = pair.strip().split()
        nums1.append(int(num1))
        nums2.append(int(num2))
nums1.sort()
nums2.sort()
for num1, num2 in zip(nums1, nums2):
    ans = ans + abs(num1 - num2)
print(ans)
