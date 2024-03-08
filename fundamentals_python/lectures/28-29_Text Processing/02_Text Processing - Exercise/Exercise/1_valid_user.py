# from icecream import ic
def is_valid_username(username):
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    return 3 <= len(username) <= 16 and \
           all(char in valid_chars for char in username) and \
           username[0] not in '-_' and username[-1] not in '-_' and \
           '--' not in username and '__' not in username and \
           '-_' not in username and '_-' not in username


def main():
    input_line = input()
    usernames = [username.strip() for username in input_line.split(',')]
    # ic(usernames)
    for username in usernames:
        if is_valid_username(username):
            print(username)


if __name__ == "__main__":
    main()
