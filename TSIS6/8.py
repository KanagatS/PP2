def unique(nums):
    s = set()
    for i in nums:
        s.add(i)
    return s


print(*unique([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]))
