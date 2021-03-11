def func1(a):
    def func2(b):
        b += 1
        return b
    a += 1
    return func2


func = func1(1)
print(func(1))
