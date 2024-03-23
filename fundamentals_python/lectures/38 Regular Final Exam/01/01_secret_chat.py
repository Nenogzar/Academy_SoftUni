secred_chat = input()

info_string = input()

while info_string != "Reveal":
    key = info_string.split(":|:")
    command = key[0]
    if command == "InsertSpace":
        space = int(key[1])
        secred_chat = secred_chat[:space]+" "+secred_chat[space:]
        print(secred_chat)

    elif command == "Reverse":
        replace_string = key[1]
        if replace_string in secred_chat:
            secred_chat =secred_chat.replace(replace_string,"",1)
            secred_chat +=replace_string[::-1]
            print(secred_chat)
        else:
            print("error")
            info_string = input()
            continue

    elif command == "ChangeAll":
        substring, replacement = key[1], key[2]
        if substring in secred_chat:
            secred_chat = secred_chat.replace(substring,replacement)
            print(secred_chat)


    info_string = input()
print(f"You have a new text message: {secred_chat}")