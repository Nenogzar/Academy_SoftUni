def collect_item(inventory, item):
    if item not in inventory:
        inventory.append(item)
    return inventory


def drop_item(inventory, item):
    if item in inventory:
        inventory.remove(item)
    return inventory


def combine_items(inventory, old_item, new_item):
    if old_item in inventory:
        index = inventory.index(old_item)
        inventory.insert(index + 1, new_item)
    return inventory


def renew_item(inventory, item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)
    return inventory

journal = input().split(", ")
command = input()

while command != "Craft!":
    comman_list = list(map(str, command.split(" - ")))
    action = comman_list[0]
    args = comman_list[1:]
    item = args[0]

    if action == "Collect":
        journal = collect_item(journal, item)
    elif action == "Drop":
        journal = drop_item(journal, item)
    elif action == "Combine Items":
        old_item, new_item = args[0].split(":")
        journal = combine_items(journal, old_item, new_item)
    elif action == "Renew":
        journal = renew_item(journal, item)

    command = input()

print(", ".join(journal))
