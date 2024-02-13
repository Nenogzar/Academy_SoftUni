while True:
    input_string = input("Въведете части на списък, разделени със запетайка: ")
    input_parts = input_string.split(',')
    my_list = input_parts
    #item=input("Item ?")
    print(my_list)
    #code
    parts = [int(part.strip()) for part in my_list]  # преобразуване от string  в  int
    print(parts)

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("10x!")
        break
