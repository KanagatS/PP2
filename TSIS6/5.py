def fact(numb):
    total = 1
    for i in range(1, numb+1):
        total *= i
    return total


print(fact(6))
