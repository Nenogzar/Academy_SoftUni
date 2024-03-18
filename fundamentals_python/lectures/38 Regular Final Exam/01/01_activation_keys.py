def contains_command(key, substring):
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")

def flip_command(key, case, start_index, end_index):
    if case == "Upper":
        key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
    elif case == "Lower":
        key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
    print(key)
    return key

def slice_command(key, start_index, end_index):
    key = key[:start_index] + key[end_index:]
    print(key)
    return key

def process_commands(raw_key):
    key = raw_key
    command = input()
    while command != "Generate":
        command_parts = command.split(">>>")
        if command_parts[0] == "Contains":
            contains_command(key, command_parts[1])
        elif command_parts[0] == "Flip":
            key = flip_command(key, command_parts[1], int(command_parts[2]), int(command_parts[3]))
        elif command_parts[0] == "Slice":
            key = slice_command(key, int(command_parts[1]), int(command_parts[2]))
        command = input()

    print(f"Your activation key is: {key}")

# Entry point of the program
if __name__ == "__main__":
    raw_key = input()
    process_commands(raw_key)
