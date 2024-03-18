def take_odd(password):
    return ''.join(password[i] for i in range(len(password)) if i % 2 != 0)

def cut_password(password, index, length):
    return password[:index] + password[index+length:]

def substitute_password(password, substring, substitute):
    if substring in password:
        return password.replace(substring, substitute)


def process(test_password):
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
