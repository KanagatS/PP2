n, m = map(int, input().split())

mx = 0
index = 0
indexmax = 0
for i in range(n):
    l = [int(i) for i in input().split()]
    if sum(l) > mx:
        mx = l
        indexmax = index

    index += 1

print(index)
