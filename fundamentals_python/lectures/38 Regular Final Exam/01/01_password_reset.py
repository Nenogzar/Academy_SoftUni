def take_odd(password):
    """

    :param password:
    :return:
    """
    return ''.join(password[i] for i in range(len(password)) if i % 2 != 0)


def cut_password(password, index, length):
    """

    :param password:
    :param index:
    :param length:
    :return:
    """
    return password[:index] + password[index + length:]


def substitute_password(password, substring, substitute):
    """

    :param password:
    :param substring:
    :param substitute:
    :return:
    """
    if substring in password:
        return password.replace(substring, substitute)


def process(test_password):
    """

    :param test_password:
    """
    password = test_password

    while True:
        command = input()
        if command == "Done":
            break
        command_part = command.split(" ")
        if command_part[0] == "TakeOdd":
            password = take_odd(password)
            print(password)
        elif command_part[0] == "Cut":
            index, length = command_part[1], command_part[2]
            password = cut_password(password, int(index), int(length))
            print(password)
        elif command_part[0] == "Substitute":
            substring, substitute_text = command_part[1], command_part[2]
            if substring in password:
                password = substitute_password(password, substring, substitute_text)
                print(password)
            else:
                print("Nothing to replace!")

    print(f"Your password is: {password}")


if __name__ == "__main__":
    test_password = input()
    process(test_password)

""" """

# test_password = input()
# password = test_password
# command = input()
# while command != "Done":
#     command_part = command.split(" ")
#     if command_part[0] == "TakeOdd":
#         password = ''.join(password[i] for i in range(len(password)) if i % 2 != 0)
#         print(password)
#     elif command_part[0] == "Cut":
#         index, length = int(command_part[1]), int(command_part[2])
#         password = password[:index] + password[index + length:]
#         print(password)
#     elif command_part[0] == "Substitute":
#         substring, substitute_text = command_part[1], command_part[2]
#         if substring in password:
#             password = password.replace(substring, substitute_text)
#             print(password)
#         else:
#             print("Nothing to replace!")
#
#     command = input()
#
# print(f"Your password is: {password}")


"""  from CEO - Python - Academy SoftUni"""

# main_string = input()
# command = input()
#
#
# def take_odd_chr(main_string):
#     result = "".join(main_string[x] for x in range(len(main_string)) if x % 2 != 0)
#     print(result)
#     return result
#
#
# def cut_string(index, length, main_string):
#     result = main_string[:index] + main_string[index + length:]
#     print(result)
#     return result
#
#
# def substitute_string(substring, substitute, main_string):
#     if substring in main_string:
#         result = main_string.replace(substring, substitute)
#         print(result)
#         return result
#     print("Nothing to replace!")
#     return main_string
#
#
# while command != "Done":
#     if "TakeOdd" in command:
#         main_string = take_odd_chr(main_string)
#         command = input()
#         continue
#     _, index_or_substring, lenght_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
#     if "Cut" in command:
#         main_string = cut_string(index_or_substring, lenght_or_substitute, main_string)
#     elif "Substitute" in command:
#         main_string = substitute_string(index_or_substring, lenght_or_substitute, main_string)
#     command = input()
#
# print(f"Your password is: {main_string}")
