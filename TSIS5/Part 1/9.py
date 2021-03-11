#line count
f = open('test.txt', 'r')
cnt = 0
for i in f:
    if i != '\n':
        cnt+=1
print(cnt)
f.close()