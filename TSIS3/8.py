a = list(input().split())
b = list(input().split())
print(' '.join(sorted(set(a).intersection(set(b)))))
