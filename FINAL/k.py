def isPower2(n):
    while n % 2 == 0:
        n /= 2
    return n == 1


l = [int(i) for i in input().split()]
s = set()

for i in range(len(l)):
    if isPower2(l[i]):
        s.add(l[i])

print(*sorted(list(s)))
