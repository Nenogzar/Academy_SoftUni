while True:
    input_string = input()

    formatted_string = input_string.replace('. ', '_').replace(' ', '_').lower()

    print(formatted_string)

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("Bay!")
        break
