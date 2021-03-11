# def file_read(file_name):
#     txt = open(file_name)
#     print(txt.read())

# file_read('test.txt')

f = open('test.txt', 'r')
print(f.read())
f.close()