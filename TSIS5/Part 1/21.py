import string

n = int(input())
f = open('alphabet.txt', 'w')
alphabet = string.ascii_uppercase
# for i in range(0, len(alphabet), n):
#     letters = (alphabet[i:i+n] + '\n')
letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]

f.writelines(letters)
f = open('alphabet.txt', 'r')
print(f.read())
f.close()
