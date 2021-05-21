#s = input().split()
d = dict()
a = ''
while True:
    s = input()
    if s != '':
        a += s + ' '
    else:
        break

a.split()
a=list(a)

for i in a:
    d[i] = d.get(i, 0) + 1
for key, value in sorted(d.items()):
    print(key + ' ' + str(value))
