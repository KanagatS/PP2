b = ''
f = open('input.txt', 'r')
content = f.read()
b += content
b = list(b)
for i in range(len(b)):
    if b[i] == ' ' or b[i] == '\n':
        b[i] = ''
    b[i] = b[i].lower()

for char in range(ord('a'), ord('z') + 1):
    print(chr(char), b.count(chr(char)), sep=' => ', end='\n')
