# needed_coffee = 0
#
# for command in iter(input, "END"):
#     if command == "coding" or command == "dog" or command == "cat" or command == "movie":
#         needed_coffee += 1
#     elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
#         needed_coffee += 2
#     else:
#         continue
#
#     if needed_coffee > 5:
#         print("You need extra sleep")
#         break
#
# else:
#     print(needed_coffee)


""" wit list"""

keywords = ["coding", "dog", "cat", "movie"]
needed_coffee = 0

for command in iter(input, "END"):
    if command in keywords:
        needed_coffee += 1
    elif command in map(str.upper, keywords):
        needed_coffee += 2
    else:
        continue

    if needed_coffee > 5:
        print("You need extra sleep")
        break

else:
    print(needed_coffee)