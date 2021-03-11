import string
n = input()
alphabet = string.ascii_lowercase
if set(alphabet) <= set(n.lower()):
    print('yes')
else:
    print('no')
