len_list = int(input("Въведи дължината на списъка: "))

num_list = []
for num in range(len_list):
    numbers = input(f"Въведи {num+1}-о число в списъка: ")
    num_list.append(int(numbers))
sort_list = sorted(num_list)
print(sort_list)

repair_list = input("Искате ли да направите корекция по списъка?(Y/N) ")

while repair_list.upper() != "N":

    sort_list[int(input(('на кои индекс? ')))] = int(input("въведи аргумент: "))
    print(sort_list)

    repeat = input("Искате ли да замените друг аргумент?(Y/N)? ")
    if repeat.upper() == "N":
        print("done")
        break

sum_lists = [num_list] + [sort_list]
zip_from_lists = list(zip(num_list, sort_list))


list1 = [item[0] for item in zip_from_lists]
list2 = [item[1] for item in zip_from_lists]

# Create a nested list
nested_list = [list1, list2]

# dict  от вложени списъци

my_dict = {key: value for key, value in zip(nested_list[0], nested_list[1])}
# Двата метода са с единтичен изход
new_dict = dict(zip(nested_list[0], nested_list[1]))

print("sum_lists ->", sum_lists)
print("zip_from_lists -> ", zip_from_lists)

print("nested_list", nested_list)
print("my_dict", my_dict)
print("new_dict", new_dict)
