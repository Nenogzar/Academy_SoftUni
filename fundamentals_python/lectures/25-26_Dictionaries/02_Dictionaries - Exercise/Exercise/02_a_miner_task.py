""" whit list """
command = input()
res_list = []
resourse_dict = {}
while command != "stop":
    res_list.append(command)
    command = input()

for i in range(0, len(res_list), 2):
    resourse = res_list[i]

    if resourse in resourse_dict:
        resourse_dict[resourse] += int(res_list[i + 1])
    else:
        resourse_dict[resourse] = int(res_list[i + 1])

for resource, quantity in resourse_dict.items():
    print(f"{resource} -> {quantity}")
# OR
# [print{resource} -> {quantity} for resource, quantity in resourse_dict.items()]


""" whit dicrionary """

mined_materials = dict()

material = input()
while material != "stop":
    quantity = int(input())

    if material not in mined_materials:
        mined_materials[material] = quantity

    elif material in mined_materials:
        mined_materials[material] += quantity

    material = input()

for resource, quantity in mined_materials.items():
    print(f"{key} -> {quantity}")

# OR
# [print {key} -> {quantity} for resource, quantity in mined_materials.items()]

"""whit get() """

resource = input()

total_resource = {}
while resource != "stop":
    quantity = int(input())
    total_resource[resource] = total_resource.get(resource, 0) + quantity
    resource = input()

for resource, quantity in total_resource.items():
    print(f"{key} -> {quantity}")