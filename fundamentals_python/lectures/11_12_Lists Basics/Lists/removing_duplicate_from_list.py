while True:
    input_string = input("Enter parts of a list separated by commas: ")
    input_parts = input_string.split(',')

    try:
        # convert string to intiger
        parts = [int(part.strip()) for part in input_parts]
        # removes duplicates
        unique_parts = list(set(parts))
        # looks for which duplicates have been removed
        removed_elements = list(set([element for element in parts if parts.count(element) > 1]))

        print(f"list without duplicates: {unique_parts}")
        print(f"Items removed from the list: {removed_elements}")
    except ValueError:
        print("Invalid input data. Please enter numeric values separated by commas.")

    repeat = input("Do you want to repeat a (Y/N)? ")
    if repeat.upper() == "N":
        print("Thanks!")
        break
