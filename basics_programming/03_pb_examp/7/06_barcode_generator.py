def generate_barcodes(start, end):
    barcodes = []
    for i in range(start, end + 1):
        barcode = str(i)
        if any(int(digit) % 2 == 0 for digit in barcode):
            continue
        barcodes.append(barcode)
    return barcodes

def generate_range(start, end):
    start_digits = [int(digit) for digit in str(start)]
    end_digits = [int(digit) for digit in str(end)]

    for first_digit in range(start_digits[0], end_digits[0] + 1):
        for second_digit in range(start_digits[1], end_digits[1] + 1):
            for third_digit in range(start_digits[2], end_digits[2] + 1):
                for fourth_digit in range(start_digits[3], end_digits[3] + 1):
                    barcode = int(f"{first_digit}{second_digit}{third_digit}{fourth_digit}")
                    if any(digit % 2 == 0 for digit in [first_digit, second_digit, third_digit, fourth_digit]):
                        continue
                    yield barcode

start = int(input())
end = int(input())

result = list(generate_range(start, end))
print(" ".join(map(str, result)))
