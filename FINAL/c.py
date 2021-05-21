a, b = [int(i) for i in input().split()], []
for i in range(len(a)):
    if a[i] != 0:
        print(a[i], end=' ')
    else:
        b.append(a[i])
print(*b)
