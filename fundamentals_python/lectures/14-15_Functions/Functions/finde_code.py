def find_numbers():
    excluded_values = [1, 4, 6, 8]

    for a in range(1, 121):
        for b in range(1, 121):
            for c in range(1, 121):
                for d in range(1, 121):
                    if (a % 3 == 0 and a % 4 == 0 and a % 5 == 0) and \
                            (b % 3 == 0 and b % 4 == 0 and b % 5 == 0 and b % 8 == 0) and \
                            (c % 3 == 0 and c % 4 == 0 and c % 5 == 0 and c % 8 == 0) and \
                            (d % 5 == 0 and d % 8 == 0) and \
                            all(x not in excluded_values for x in [a, b, c, d]):
                        return a, b, c, d


result = find_numbers()
print("A, B, C, D =", result)
