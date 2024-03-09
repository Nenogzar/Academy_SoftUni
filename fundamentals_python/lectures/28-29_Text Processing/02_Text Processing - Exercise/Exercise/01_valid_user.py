# # from icecream import ic
# def is_valid_username(username):
#     len_name_username = len(username)
#     return 3 <= len_name_username <= 16 and \
#            all(char.isalpha() or char.isdigit() or char in '-' or char in '_' for char in username)
#
#
# def main():
#     input_line = input()
#     usernames = [username.strip() for username in input_line.split(',')]
#     # ic(usernames)
#     for username in usernames:
#         # ic(username)
#         if is_valid_username(username):
#             print(username)
#
#
# if __name__ == "__main__":
#     main()

""" """
# def is_valid_name(name):
#     # Проверка за дължина
#     if not (3 <= len(name) <= 16):
#         return False
#
#     # Проверка за валидни символи
#     for character in name:
#         if not (character.isalnum() or character == "-" or character == "_"):
#             return False
#
#     # Проверка за празни полета
#     def no_redundant_symbols(name):
#         if " " in name:
#             return False
#
#     return True
#
#
# def username_is_valid(name):
#     if is_valid_name(name):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if username_is_valid(username):
#         print(username)


""" CEO """
usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char not in "-_" + string.ascii_letters + string.digits:
                break

        else:
            print(username)
