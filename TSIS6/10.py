def even(nums):
    lst = []
    for i in nums:
        if i % 2 == 0:
            lst.append(i)
    return lst


print(*even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
