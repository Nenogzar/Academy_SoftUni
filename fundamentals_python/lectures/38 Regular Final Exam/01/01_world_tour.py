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

