n, m = map(int, input().split())

mx, indexmax = 0, 1

for index in range(1, n+1):
    l = [int(i) for i in input().split()]
    if sum(l) > mx:
        mx = sum(l)
        indexmax = index

print(indexmax)
