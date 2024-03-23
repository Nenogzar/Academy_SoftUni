import re

num_inputs = int(input())

default_group = "00"
pattern = re.compile(r"@[#]+(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+")

for _ in range(num_inputs):
    input_str = input()
    matches = pattern.finditer(input_str)
    found = False

    for match in matches:
        found = True
        barcode = match.group('barcode')
        #barcode_group = "".join(filter(str.isdigit, barcode))  # same
        barcode_group = "".join(b for b in barcode if b.isdigit())
        if barcode_group:
            print(f"Product group: {barcode_group}")
        else:
            print(f"Product group: {default_group}")

    if not found:
        print("Invalid barcode")

""" CEO"""
#
# import re
#
# number_products_to_scan = int(input())
# default_barcode = "00"
# group_d = "Product group:"
# patterns = re.compile(r"@[#]+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+")
# for _ in range(number_products_to_scan):
#     bar_code = input()
#     main_string = re.finditer(patterns, bar_code)
#     found = False
#     for a in main_string:
#         found = True
#         result = "".join(x for x in a["found_text"] if x.isdigit())
#         if result:
#             print(f"{group_d} {result}")
#         else:
#             print(f"{group_d} {default_barcode}")
#     if not found:
#         print("Invalid barcode")


"""kumchyovalcho"""

# import re
# count_of_barcodes = int(input())
# for _ in range(count_of_barcodes):
#     current_barcode = input()
#     pattern = re.compile(r'(@#{1,})(?P<barcode>[A-Z][A-Za-z\d]{4,}[A-Z])(@#{1,})')
#     digits = re.compile(r'(?P<digits>\d+)')
#     barcode_validation = list(pattern.finditer(current_barcode))
#     digits_finder = list(digits.finditer(current_barcode))
#     if barcode_validation:
#         if digits_finder:
#             digit = [digit['digits'] for digit in digits_finder]
#             if digit:
#                 print(f"Product group: {''.join(digit)}")
#         elif not digits_finder:
#             print("Product group: 00")
#     elif not barcode_validation:
#         print("Invalid barcode")
