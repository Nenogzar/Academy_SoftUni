from icecream import ic
user = input()


register = input()
while register != "Registration":
    key = register.split(" ")
    ic(key)
    command = key[0]
    if command == 'Letters':
        pass
        if key[1] == 'Lower':
            letter = key[1].lower()
        elif key[1] == 'Upper':
            letter == key[1].upper()
        print(letter)
    elif command == 'Reverse':
        pass
    elif command == 'Substring':
        pass
    elif command == 'Replace':
        pass
    elif command == 'IsValid':
        pass





    register = input()





"""

John
Letters Lower
Substring SA
IsValid @
Registration

asdad

ThisIsSoftUni
Reverse 1 3
Replace S
Substring hi
Registration
"""
