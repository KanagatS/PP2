def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

l =[]
while True:
    s = int(input())
    if s != '':
        l.append(s)
    else:
        break

l1 = set()

for i in range(len(l)):
    if not isPrime(l[i]) and l.count(l[i]) > 1:
        l1.add(l[i])

print(*l1)
