def check(n, a, b):
    if n in range(a, b):
        return 'YES'
    else:
        return 'NO'


n = int(input('Enter the number: '))
a = int(input('Enter the start of range: '))
b = int(input('Enter the end of range: '))

print(check(n, a, b))
