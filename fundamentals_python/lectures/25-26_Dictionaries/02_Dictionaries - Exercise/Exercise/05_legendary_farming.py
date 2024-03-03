input_items = input().split()
item_useful = {"shards": 0, "fragments": 0, "motes": 0}
item_useless = {}

obtained = False

while True:
    for i in range(0, len(input_items), 2):
        quantity = int(input_items[i])
        material = input_items[i + 1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            item_useful[material] += quantity
        else:
            if material not in item_useless:
                item_useless[material] = quantity
            else:
                item_useless[material] += quantity
        if item_useful["motes"] >= 250:
            print("Dragonwrath obtained!")
            item_useful["motes"] -= 250
            obtained = True
            break
        elif item_useful["fragments"] >= 250:
            print("Valanyr obtained!")
            item_useful["fragments"] -= 250
            obtained = True
            break
        elif item_useful["shards"] >= 250:
            print("Shadowmourne obtained!")
            item_useful["shards"] -= 250
            obtained = True
            break
    if obtained:
        break
    input_items = input().split()


for keys, value in item_useful.items():
    print(f"{keys}: {value}")
for keys, value in item_useless.items():
    print(f"{keys}: {value}")

