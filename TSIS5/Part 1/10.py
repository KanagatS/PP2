#count of each word in file

from collections import Counter
f = open('test.txt', 'r')
print(Counter(f.read().split()))