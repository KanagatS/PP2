import random
f = open('test.txt', 'r')
line = f.read().splitlines()
print(random.choice(line))