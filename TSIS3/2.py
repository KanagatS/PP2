a = list(input().split())
mn = 1000
for i in range(len(a)):
    if (int(a[i]) > 0) and (int(a[i]) < mn):
        mn = int(a[i])
print(mn)
