s, d = input(), dict()

print(len(set(s)))
for i in s:
    d[i] = d.get(i, 0) + 1

for k, v in sorted(d.items()):
    print(k + ' ' + str(v))
