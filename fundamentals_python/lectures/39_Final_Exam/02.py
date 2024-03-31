# import re
#
#
# def find_eggs(shifer):
#     pattern = r'([\@|\#])([a-z]{3,})([\@|\#+)([^A-Za-z0-9]+?)\/+(\d+)\/+'
#     color_eggs = re.findall(pattern, shifer)
#     for color, amount in color_eggs:
#         print(f"You found {amount} {color} eggs!")
#
# shifer = input()
# find_eggs(shifer)


# import re
#
#
# def find_eggs(shifer):
#     pattern = r"([\@|\#]+)([a-z]{3,})([\@|\#]+)([^A-Za-z0-9]+?)\/+\d+\/+"
#     color_eggs = re.finditer(pattern, shifer)
#     for egg in color_eggs:
#         color = egg.group('color')
#         amount = egg.group('amount')
#         print(f"You found {amount} {color} eggs!")
#
#
# shifer = input()
# find_eggs(shifer)


# import re
#
# def find_eggs(shifer):
#     pattern = r'(([\@|\#]+)([a-z]{3,})([\@|\#]+)([^A-Za-z0-9]+?)\/+(\d+)\/+)'
#     color_eggs = re.findall(pattern, shifer)
#     for _, color1, egg_type, color2, _, amount in color_eggs:
#         print(f"You found {amount} {egg_type} eggs!")
#
# shifer = input()
# find_eggs(shifer)

import re


def find_eggs(shifer):
    pattern = r'(([\@|\#]+)([a-z]{3,})([\@|\#]+)([^A-Za-z0-9]+)?\/+(\d+)\/+)'
    color_eggs = re.findall(pattern, shifer)

    if color_eggs:  # Check if there are any matches
        for egg in color_eggs:
            print(f"You found {egg[5]} {egg[2]} eggs!")


shifer = input()
find_eggs(shifer)
