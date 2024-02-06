""" 1 nested list"""
num_list = list()
export_list = list()
while True:
    to_do_list = input()
    if to_do_list == "End":
        break

    tasks = to_do_list.split("-")
    nested_list = [task.strip() for task in tasks]
    num_list.append(nested_list)

num_list.sort(key=lambda x: int(x[0]))

# print(num_list)

for nested_list in num_list:
    export_list.append(nested_list[1])
print(export_list)

""" 2  tuple """

to_do_list = input()

num_list = list()

while to_do_list != "End":
    importance, note = map(str.strip, to_do_list.split("-"))
    num_list.append((int(importance), note))

    to_do_list = input()

num_list.sort(key=lambda x: x[0])

export_list = [note for _, note in num_list]
print(export_list)