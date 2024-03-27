user_name = input()

register = input()
while register != "Registration":
    key = register.split(" ")
    command = key[0]

    if command == 'Letters':
        do_it = key[1]
        if do_it == 'Lower':
            user_name = user_name.lower()
        elif do_it == 'Upper':
            user_name = user_name.upper()
        print(user_name)

    elif command == 'Reverse':
        start_index, end_index = int(key[1]), int(key[2])
        if 0 <= start_index < len(user_name) and 0 <= end_index < len(user_name):
            reversed_string = user_name[start_index: end_index + 1][::-1]
            print(reversed_string)

    elif command == 'Substring':
        given_substring = key[1]
        if given_substring in user_name:
            user_name = user_name.replace(given_substring, "")
            print(user_name)
        else:
            print(f"The username {user_name} doesn't contain {given_substring}.")

    elif command == 'Replace':
        replace_char = key[1]
        user_name = user_name.replace(replace_char, "-")
        print(user_name)

    elif command == 'IsValid':
        char_to_check = key[1]
        if char_to_check in user_name:
            print("Valid username.")
        else:
            print(f"{char_to_check} must be contained in your username.")

    register = input()
