#last n lines of code

f = open('test.txt', 'r')
n = int(input())
lines = f.readlines()
last_lines = lines[-n:]
print(*last_lines)