def is_prime(numb):
    if (numb == 1):
        return False

    for i in range(2, numb):
        if numb % i == 0:
            return False

    return True


n = int(input())
print(is_prime(n))
