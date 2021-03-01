""" a = list(input().split())
for i in range(len(a)):
    if a[i] == '0':
        del a[i]
        a.append('0')
print(' '.join(a))
 """


a = [int(i) for i in input().split()]
b = 0
for i in range(len(a)):
    if a[i] != 0:
        print(a[i], end=" ")
    else:
        b = b + 1
for i in range(b):
    print(0, end=" ")
