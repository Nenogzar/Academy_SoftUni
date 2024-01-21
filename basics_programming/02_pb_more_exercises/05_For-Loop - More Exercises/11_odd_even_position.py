numbers = int(input())

evan_sum = 0
evan_max = float('-inf')
evan_min = float('inf')

odd_sum = 0
odd_max = float('-inf')
odd_min = float('inf')

for num in range(1, numbers + 1):
    check_number = float(input())

    if num % 2 == 0:  # Even position
        evan_sum += check_number
        evan_max = max(evan_max, check_number)
        evan_min = min(evan_min, check_number)
    else:  # Odd position
        odd_sum += check_number
        odd_max = max(odd_max, check_number)
        odd_min = min(odd_min, check_number)


print(f"OddSum={odd_sum:.2f},")
if odd_min == float('inf'):
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == float('-inf'):
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={evan_sum:.2f},")
if evan_min == float('inf'):
    print("EvenMin=No,")
else:
    print(f"EvenMin={evan_min:.2f},")
if evan_max == float('-inf'):
    print("EvenMax=No")
else:
    print(f"EvenMax={evan_max:.2f}")
