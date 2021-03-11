# f1 = open('from.txt', 'r')
# f2 = open('to.txt', 'w')
# for i in f1:
#     f2.write(i)

# f2 = open('to.txt', 'r')
# print(f2.read())

from shutil import copyfile
copyfile('from.txt', 'to.txt')