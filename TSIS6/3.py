def sum(nums):
    cnt = 1
    for i in nums:
        cnt *= i
    return cnt


print(sum([1, 2, 3, 4, 5]))
