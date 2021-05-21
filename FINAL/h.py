import sys

s = sys.stdin.read().split()
d = dict()

for i in range(0, len(s), 2):
    if s[i] not in d:
        d[s[i]] = s[i+1]
    elif s[i+1] > d[s[i]]:
        d[s[i]] = s[i+1]

for k, v in sorted(d.items()):
    print(k, v)
