n = int(input())
start = 0
for i in range(n):
    l = [int(i) for i in range(start, start + n)]
    print(*l)
    start += 1
