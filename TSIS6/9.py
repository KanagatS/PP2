def is_prime(numb):
    if (numb == 1):
        return False

    for i in range(2, numb):
        if nums % i == 0:
            return False
    
    return True


print(is_prime(2))
