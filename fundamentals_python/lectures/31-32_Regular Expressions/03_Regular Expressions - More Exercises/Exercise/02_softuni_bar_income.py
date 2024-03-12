import re

total_sum = 0

while True:
    record = input()
    if record == "end of shift":
        break

    match = re.match(r'%([A-Z][a-z]*)%.*?<([^>]+)>.*?\|(\d+)\|.*?([\d.]+)\$', record)
    if match:
        customer_name = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))

        total_price = count * price
        total_sum += total_price

        print(f"{customer_name}: {product} - {total_price:.2f}")

print(f"Total income: {total_sum:.2f}")


#
# import re
#
# total_sum = 0
#
# while True:
#     record = input()
#     if record == "end of shift":
#         break
#
#     # Validate the order using regular expressions
#     match = re.match(r'%([A-Z][a-z]*)%.*?<([^>]+)>.*?\|(\d+)\|.*?([\d.]+)\$', record)
#     if match:
#         customer_name = match.group(1)
#         product = match.group(2)
#         count = int(match.group(3))
#         price = float(match.group(4))
#
#         # Check for text between groups
#         text_between_groups = re.search(r'%([A-Z][a-z]*)%.*?<([^>]+)>\|(\d+)\|([\d.]+)\$(.*?)$', record)
#         if text_between_groups:
#             text = text_between_groups.group(5)
#             # Process the text as needed
#
#         total_price = count * price
#         total_sum += total_price
#
#         print(f"{customer_name}: {product} - {total_price:.2f}")
#
# print(f"Total income: {total_sum:.2f}")
