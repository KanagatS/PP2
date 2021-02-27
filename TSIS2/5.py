n = input()
sm, prdct = 0, 1
for i in range(len(n)):
    sm += int(n[i])
    prdct *= int(n[i])
print(prdct - sm)
