def is_prime(prime):
    if prime <= 1:
        return False

    i = 2
    while i <= prime // 2:
        if prime % i == 0:
            return False
        i += 1

    return True

# Пример на използване на функцията
prime = int(input("Въведете число: "))
if is_prime(prime):
    print(f"{prime} е просто число")
else:
    print(f"{prime} не е просто число")
