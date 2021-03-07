def cnt(str):
    ucase, dcase = 0, 0
    for i in str:
        if i.isupper():
            ucase += 1
        else:
            dcase += 1
    return ucase, dcase


s = input()
print(*cnt(s))
