def unique(nums):
    s = set()
    for i in nums:
        s.add(i)
    return s

lst = input().split()
print(*unique(lst))
