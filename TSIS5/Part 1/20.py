import string
import os

for i in string.ascii_lowercase:
    open(i + '.txt', 'x')
