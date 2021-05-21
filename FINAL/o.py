s = [i.upper() for i in input().split()]
cnt = []

for i in range(len(s)):
    cnt.append(s.count(s[i]))

idx = cnt.index(max(cnt))

print(s[idx])
