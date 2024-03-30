number_of_pieces = int(input())
piece_info = {}


for song in range(number_of_pieces):
    info = input().split("|")
    piece, composer, key = info[0], info[1], info[2]
    piece_info[piece] = {'composer': composer, 'key':key}

command = input()
while command != "Stop":
    command = command.split("|")
    action, piece = command[0], command[1]
    if action == "Add":
        if piece in piece_info:
            print(f"{piece} is already in the collection!")
        else:
            composer, key = command[2], command[3]
            piece_info[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece not in  piece_info:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del piece_info[piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece not in piece_info:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Changed the key of {piece} to {new_key}!")
            piece_info[piece]['key'] = new_key


    command = input()

for piece, detail in piece_info.items():
    print(f"{piece} -> Composer: {detail['composer']}, Key: {detail['key']}")
