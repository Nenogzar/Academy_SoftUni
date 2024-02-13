""" 1 """
password = input()
error_messages = []

if not 6 <= len(password) <= 10:
    error_messages.append("Password must be between 6 and 10 characters")
if not password.isalnum():
    error_messages.append("Password must consist only of letters and digits")
if sum(1 for x in password if x.isdigit()) < 2:
    error_messages.append("Password must have at least 2 digits")

if error_messages:
    print(*error_messages, sep='\n')
else:
    print("Password is valid")

""" 2 """


def is_valid_password(password):
    if not 6 <= len(password) <= 10:
        return "Password must be between 6 and 10 characters"
    if not password.isalnum():
        return "Password must consist only of letters and digits"
    if sum(1 for c in password if c.isdigit()) < 2:
        return "Password must have at least 2 digits"

    return "Password is valid"


user_password = input()
result = is_valid_password(user_password)
print(result)

""" 3 """


def password_validator(password):
    errors = []

    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    if sum(char.isdigit() for char in password) < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


user_password = input()
password_validator(user_password)
