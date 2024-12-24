ans = 0
puzzle: dict[list[int]] = {}
with open('07.data') as file:
    for line in file:
        target, nums = line.strip().split(': ')
        assert int(target) not in puzzle
        puzzle[int(target)] = [int(_) for _ in nums.split()]


def dfs(target: int, curr: int, idx: int, nums: list[int]) -> bool:
    if curr > target:
        return False
    if idx == len(nums):
        return curr == target
    return dfs(target, curr + nums[idx], idx + 1, nums) or \
        dfs(target, curr * nums[idx], idx + 1, nums) or \
        dfs(target, int(str(curr) + str(nums[idx])), idx + 1, nums)


for target, nums in puzzle.items():
    if dfs(target, nums[0], 1, nums):
        ans = ans + target
print(ans)
