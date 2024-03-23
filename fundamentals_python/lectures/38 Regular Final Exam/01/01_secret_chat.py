# secred_chat = input()
#
# info_string = input()
#
# while info_string != "Reveal":
#     key = info_string.split(":|:")
#     command = key[0]
#     if command == "InsertSpace":
#         space = int(key[1])
#         secred_chat = secred_chat[:space]+" "+secred_chat[space:]
#         print(secred_chat)
#
#     elif command == "Reverse":
#         replace_string = key[1]
#         if replace_string in secred_chat:
#             secred_chat =secred_chat.replace(replace_string,"",1)
#             secred_chat +=replace_string[::-1]
#             print(secred_chat)
#         else:
#             print("error")
#             info_string = input()
#             continue
#
#     elif command == "ChangeAll":
#         substring, replacement = key[1], key[2]
#         if substring in secred_chat:
#             secred_chat = secred_chat.replace(substring,replacement)
#             print(secred_chat)
#
#
#     info_string = input()
# print(f"You have a new text message: {secred_chat}")




main_msg = input()
info_string = input()


while info_string != "Reveal":
    key, *manipulation = info_string.split(":|:")

    found_error = False
    if key == "ChangeAll":
        main_msg = main_msg.replace(manipulation[0], manipulation[1])

    elif key == "Reverse":
        substring = manipulation[0]
        if substring not in main_msg:
            print("error")
            found_error = True
        else:
            main_msg = main_msg.replace(substring, "", 1) + substring[::-1]

    elif key == "InsertSpace":
        index_for_insert = int(manipulation[0])
        main_msg = main_msg[:index_for_insert] + " " + main_msg[index_for_insert:]

    if not found_error:
        print(main_msg)

    info_string = input()

print(f"You have a new text message: {main_msg}")