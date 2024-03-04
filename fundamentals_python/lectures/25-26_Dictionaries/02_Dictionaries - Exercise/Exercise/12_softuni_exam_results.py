# university = {}
# language_counts = {}
# collect = input()
#
# while collect != "exam finished":
#     if "banned" in collect.split("-"):
#         username = collect.split("-")[0]
#         del university[username]
#     else:
#         username, language, points = collect.split("-")
#         language_counts[language] = language_counts.get(language, 0) + 1
#         points = int(points)
#         if username not in university:
#             university[username] = {language: points}
#         else:
#             if language not in university[username]:
#                 university[username][language] = points
#             else:
#                 if points > university[username][language]:
#                     university[username][language] = points
#
#     collect = input()
# print(university)
# print(language_counts)
# print("Results:")
# for user, scores in university.items():
#     for language, points in scores.items():
#         print(f"{user} | {points}")
#
# print("Submissions:")
# for language, count in language_counts.items():
#     print(f"{language} - {count}")

""" """

university = {}

collect = input()
while collect != "exam finished":
    if "banned" in collect.split("-"):
        username = collect.split("-")[0]
        del university[language]["users"][username]
    else:
        username, language, points = collect.split("-")
        points = int(points)
        if language not in university:
            university[language] = {"count": 1, "users": {username: points}}
        else:
            university[language]["count"] += 1
            if username not in university[language]["users"]:
                university[language]["users"][username] = points
            else:
                if points > university[language]["users"][username]:
                    university[language]["users"][username] = points

    collect = input()

print("Results:")
for language, data in university.items():
    for user, points in data["users"].items():
        print(f"{user} | {points}")

print("Submissions:")
for language, data in university.items():
    print(f"{language} - {data['count']}")

