f = open('test.txt', 'w')
l = input().split()
for i in l:
    f.write(i)
    f.write('\n')
f = open('test.txt', 'r')
print(f.read())
f.close()