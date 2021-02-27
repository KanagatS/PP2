s, t = input(), ''
for i in range(len(s)):
    if s[i] == 'G':
        t += 'G'
    if s[i] == '(':
        if s[i + 1] == ')':
            t += 'o'
        elif s[i+1] == 'a' and s[i+2] == 'l':
            t += 'al'
print(t)
