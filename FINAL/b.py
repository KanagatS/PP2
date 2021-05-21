import sys

s = input()
a = sys.stdin.read().split()

res = set()

for i in range(len(a)):
    if sorted(s) != sorted(a[i]):
        res.add(a[i])


print(*sorted(list(res)))
