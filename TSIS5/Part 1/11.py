import os
#
stat_info = os.stat('test.txt')
print(stat_info.st_size)