import sys

l = sys.stdin.read().split()

d = dict()

for i in l:
    d[i] = d.get(i, 0) + 1

for key, value in sorted(d.items()):
    print(key + ' ' + str(value))
