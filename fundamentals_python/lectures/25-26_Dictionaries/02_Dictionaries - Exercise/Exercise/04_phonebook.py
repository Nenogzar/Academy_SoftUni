phone_book = {}
phone_number = input()
while not phone_number.isdigit():
    name, number = phone_number.split("-")
    phone_book[name] = phone_book.get(name, number)
    phone_number = input()

for _ in range(int(phone_number)):
    name_check = input()
    if name_check in phone_book:
        print(f"{name_check} -> {phone_book[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")

####################

phone_book = {}

input_data = input()

while not input_data.isdigit():
    parts = input_data.split("-")
    if len(parts) == 2:
        name = parts[0].strip()
        phone = parts[1].strip()
        phone_book[name] = phone
    input_data = input()

num = int(input_data)

for _ in range(num):
    check_name = input()
    if check_name in phone_book:
        print(f"{check_name} -> {phone_book[check_name]}")
    else:
        print(f"Contact {check_name} does not exist.")