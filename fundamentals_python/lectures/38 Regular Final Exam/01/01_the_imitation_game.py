def move_operation(message, number_of_letters):
    """

    :param message:
    :param number_of_letters:
    :return:
    """
    return message[number_of_letters:] + message[:number_of_letters]


def insert_operation(message, index, value):
    """

    :param message:
    :param index:
    :param value:
    :return:
    """
    return message[:index] + value + message[index:]


def change_operation(message, substring, replacement):
    """

    :param message:
    :param substring:
    :param replacement:
    :return:
    """
    return message.replace(substring, replacement)


encrypted_message = input()
receiving_strings = input()

while receiving_strings != "Decode":
    instructions = receiving_strings.split("|")
    operation = instructions[0]

    if operation == "Move":
        encrypted_message = move_operation(encrypted_message, int(instructions[1]))
    elif operation == "Insert":
        index = int(instructions[1])
        value = instructions[2]
        encrypted_message = insert_operation(encrypted_message, index, value)
    elif operation == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        encrypted_message = change_operation(encrypted_message, substring, replacement)

    receiving_strings = input()

print(f"The decrypted message is: {encrypted_message}")
