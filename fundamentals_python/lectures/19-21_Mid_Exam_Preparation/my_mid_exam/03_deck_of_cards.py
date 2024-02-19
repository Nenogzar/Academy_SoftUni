def add_card(list_card, card_name):
    if card_name not in list_card:
        list_card.append(card_name)
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def remove_card(list_card, card_name):
    if card_name in list_card:
        list_card.remove(card_name)
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_index_card(list_card, index):
    if 0 <= index < len(list_card):
        list_card.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")


def insert_card(list_card, index, card_name):
    if abs(index) <= len(list_card):
        if card_name not in list_card:
            list_card.insert(index, card_name)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")


cards_list = list(map(str, input().split(", ")))
manipulation_range = int(input())

for _ in range(manipulation_range):
    command = list(map(str, input().split(", ")))

    manipulation = command[0]

    if len(command) == 3:
        card_name = command[2]
        position = int(command[1])
        if manipulation == "Insert":
            insert_card(cards_list, position, card_name)
        else:
            print("Invalid command format")
    elif len(command) == 2:
        if manipulation == "Add":
            add_card(cards_list, command[1])
        elif manipulation == "Remove":
            remove_card(cards_list, command[1])
        elif manipulation == "Remove At":
            position = int(command[1])
            remove_index_card(cards_list, position)

# print(cards_list)
print(",".join(cards_list))
