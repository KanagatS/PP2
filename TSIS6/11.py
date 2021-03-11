def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        return 'YES'
    else:
        return 'NO'


print(perfect_number(4))
