def isPalindrome(s):
    return s == s[::-1]

l = [i for i in input().split()]
s = set()

for i in range(len(l)):
    if not isPalindrome(l[i]):
        s.add(l[i])

print('\n'.join(sorted(list(s))))
