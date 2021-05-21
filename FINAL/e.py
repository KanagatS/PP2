import sys

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


l = sys.stdin.read().split()
s = set()

for i in range(len(l)):
    if not isPrime(l[i]) and l.count(l[i]) > 1:
        s.add(l[i])

print(*s)
