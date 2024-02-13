voldemort_flag = False
name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldemort_flag = True
        break  # Прекратява изпълнението на кода, ако се въведе "Voldemort"

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if not voldemort_flag:
    print("Welcome to Hogwarts.")


"""  OLD Exercise"""

# name = input()
# going_to = {
#     "Gryffindor": 5,
#     "Slytherin": 6,
#     "Ravenclaw": 7,
#     "Hufflepuff": 100
# }
#
# while name != "Welcome!":
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#     for destination, num in going_to.items():
#         if len(name) < num:
#             print(f"{name} goes to {destination}.")
#             break
#     name = input()
# else:
#     print("Welcome to Hogwarts.")

""" 1 """



# while True:
#     name = input()
#     if name == "Welcome!":
#         print("Welcome to Hogwarts.")
#         break
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#
#     elif 5 <= len(name) < 6:
#         print(f"{name} goes to Slytherin.")
#
#     elif len(name) < 7:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")




