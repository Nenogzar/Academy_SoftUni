# from icecream import ic
def is_valid_username(username):
    len_name_username = len(username)
    return 3 <= len_name_username <= 16 and \
           all(char.isalpha() or char.isdigit() or char in '-' or char in '_' for char in username)


def main():
    input_line = input()
    usernames = [username.strip() for username in input_line.split(',')]
    # ic(usernames)
    for username in usernames:
        # ic(username)
        if is_valid_username(username):
            print(username)


if __name__ == "__main__":
    main()
