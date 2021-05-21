a, b, c, d = map(int, input().split())

for i in range(-1000, 1001):
    if a*i-b == c*i+d:
        print(i)
        break
