    #премахване на item от листа my_list

while True:
                                    # дефиниране на променлива която присвоява текст
    input_string = input("Въведете цели числа, разделени със запетайка: ")
    input_parts = input_string.split(',')
    my_list = input_parts
    item=input("Item ? ")

    me_list = [x for x in my_list if x.strip() != item]
    print(f"{me_list = }")

    parts = [int(part.strip()) for part in my_list]
    print(f"{parts = }")

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("10x!")
        break