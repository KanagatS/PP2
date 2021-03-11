def check(n, a, b):
    if n in range(a, b):
        return 'YES'
    else:
        return 'NO'


n, a, b = map(int, input().split())

print(check(n, a, b))
