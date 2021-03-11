f = open('test.txt', 'r')
l = []
l.append(f.readlines())
print(*l)
