a, b, k = map(int, input().split())
s = []
for i in range(1, max(a, b) + 1):
    if a % i == 0 and b % i == 0:
        s.append(i)

print(s[len(s)-k])
