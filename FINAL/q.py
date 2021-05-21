n, m = map(int, input().split())

l = [0] * n
for i in range(n):
    l[i] = [0] * m

for i in range(n):
    for j in range(m):
        if i < n/2 and j < m/2:
            l[i][j] = 1
        elif i < n/2 and j >= m/2:
            l[i][j] = 0
        elif i >= n/2 and j < m/2:
            l[i][j] = 2
        elif i >= n/2 and j >= m/2:
            l[i][j] = 3

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=' ')
    print()
