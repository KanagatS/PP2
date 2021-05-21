def good(n):
    while n % 3 == 0:
        n /= 3
    return n == 1


a, b = map(int, input().split())
for i in range(b, a, -1):
    if good(i) and len(str(i)) == 4:
        print(i)
