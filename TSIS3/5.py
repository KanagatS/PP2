a = list(input().split())
k = abs(int(input()))
a = a[k:] + a[:k]
print (' '.join(a))