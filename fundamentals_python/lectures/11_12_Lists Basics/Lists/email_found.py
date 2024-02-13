# import re
#
#
# spisak = open("split.txt")
# for line in spisak:
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     found = re.findall(pattern, line)
#     for email in found:
#         email_split = email.split("@")
#         user = email_split[0]
# #        print(email)
# #        print(email_split)
#         print(user)

"""""""-с експортиране във файл user.txt  на резултатите-"""""""

import re

# Отваряне на текстовия файл за четене
spisak = open("split.txt")

# Създаване на файл за запис на резултата
with open("user.txt", "w") as user_file:
    for line in spisak:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        found = re.findall(pattern, line)
        for email in found:
            email_split = email.split("@")
            user = email_split[0]
            # Записване на 'user' във файла 'user.txt'
            user_file.write(user + '\n')


