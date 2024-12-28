from functools import cache


with open('11.data') as file:
    nums = [int(_) for _ in file.readline().strip().split()]


@cache
def dfs(num: int, step: int) -> int:
    if not step:
        return 1
    if not num:
        return dfs(1, step - 1)
    num_len = len(str(num))
    if not num_len % 2:
        left, right = divmod(num, 10 ** (num_len // 2))
        return dfs(left, step -1) + dfs(right, step -1)
    return dfs(num * 2024, step - 1)


print(sum(dfs(_, 75) for _ in nums))
