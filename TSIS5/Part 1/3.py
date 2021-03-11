f = open('test.txt', 'a')
n = input()
f.write(n)
f.close()

f = open('test.txt', 'r')
print(f.read())
f.close()