chat_num = int(input())
message = ""
for _ in range(chat_num):
    message_num = int(input())

    if message_num == 88:
        message = "Hello"
    elif message_num == 86:
        message = "How are you?"
    elif message_num < 88:
        message = "GREAT!"
    else: # elif message_num > 88:
        message = "Bye."
    print(message)


""" 2 """

numbers_to_check = int(input())

for _ in range(numbers_to_check):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num < 88:
        print("GREAT!")
    elif num > 88:
        print("Bye.")