str, a = input(), []
res = set()

while True:
    s = input()
    if s != '':
        a.append(s)
    else:
        break

for i in range(len(a)):
    if sorted(str) != sorted(a[i]):
        res.add(a[i])


print(*sorted(list(res)))
