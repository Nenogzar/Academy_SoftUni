containing_string = input()
command = input()

while command != "Travel":
    command_type, start_index_or_str, end_index_or_str = [int(x) if x.isdigit() else x for x in command.split(":")]
    if "Switch" in command_type:
        containing_string = containing_string.replace(start_index_or_str, end_index_or_str)
    elif "Add Stop" in command_type:
        if 0 <= start_index_or_str < len(containing_string):
            containing_string = f"{containing_string[:start_index_or_str]}{end_index_or_str}{containing_string[start_index_or_str:]}"
    elif "Remove Stop" in command_type:
        if 0 <= start_index_or_str < len(containing_string) and 0 <= end_index_or_str < len(containing_string):
            containing_string = f"{containing_string[:start_index_or_str]}{containing_string[end_index_or_str + 1:]}"
    print(containing_string)
    command = input()

print(f"Ready for world tour! Planned stops: {containing_string}")

""" CEO """


# travel_place = input()
#
#
# def main():
#     command = input()
#     while command != "Travel":
#         command = command.split(":")
#         if "Add Stop" in command[0]:
#             add(int(command[1]), command[2])
#
#         elif "Remove Stop" in command[0]:
#             remove(int(command[1]), int(command[2]))
#
#         elif command[0] == "Switch":
#             switch(command[1], command[2])
#
#         print(travel_place)
#         command = input()
#     print(f"Ready for world tour! Planned stops: {travel_place}")
#
#
# def add(index, string):
#     global travel_place
#     if 0 <= index < len(travel_place):
#         travel_place = f"{travel_place[:index]}{string}{travel_place[index:]}"
#
#
# def remove(start_index, end_index):
#     global travel_place
#     if 0 <= start_index and end_index < len(travel_place):
#         travel_place = f"{travel_place[:start_index]}{travel_place[end_index + 1:]}"   # ending_index is  + 1 to jump over the last letter of the word
#
#
# def switch(old_string, new_string):
#     global travel_place
#     if old_string in travel_place:
#         travel_place = travel_place.replace(old_string, new_string)
#
#
# main()