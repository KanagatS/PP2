f1 = open('test.txt', 'r')
f2 = open('test2.txt', 'r')
for l1, l2 in zip(f1, f2):
    print(l1 + l2)