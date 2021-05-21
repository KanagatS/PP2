n = int(input())
s = list(map(int, input().split()))
mx = max(s)
for i in range(len(s)):
    if s[i] == mx:
        s[i] = 1
    else:
        s[i] = 0

print(*s)
