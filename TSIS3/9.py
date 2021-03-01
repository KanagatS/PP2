Anya, Boris = list(map(int, input().split()))
a, b = set(), set()

for i in range(Anya):
    a.add(int(input()))
for i in range(Boris):
    b.add(int(input()))

print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))