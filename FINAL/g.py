import sys

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
s = [i for i in sys.stdin.read().split()]

for i in alphabet:
    cnt = 0
    for j in s:
        if i == j[0]:
            cnt += 1
    print(cnt)
