n = int(input())
d = {}
for i in range(0, n):
    first, second = input().split()
    d[first] = second
    d[second] = first
k = input()
print(d[k])
