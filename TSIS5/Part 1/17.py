f = open('test.txt', 'r')
line_without_newlines = ''

for i in f:
    line_without_newlines += i.rstrip()

print(line_without_newlines)