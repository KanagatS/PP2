def toSeven(n):
    if n == 0:
        return 0
    res = ''
    while n != 0:
        mod = n % 7
        n //= 7
        res += str(mod)

    return res[::-1]


print(toSeven(int(input())))
