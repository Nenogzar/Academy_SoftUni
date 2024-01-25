num_lists = int(input("Въведете брой на списъците: "))
min_values_list = []
for i in range(num_lists):
    input_list = [int(x) for x in input(f"Въведете списък от числа разделен с интервал.  Списък:{i + 1}: ").split()]
                # input_list = list(map(int, input(f"Въведете списък от числа разделен с интервал.  Списък: {i + 1}: ").split()))
    if not input_list:
        print("Празен списък. Пропускане.")
        continue

    # Намиране на минималната стойност в текущия списък и добавяне в новия лист
    min_value = min(input_list)
    min_values_list.append(min_value)
max_item = max(min_values_list)
# Извеждане на новия лист с минималните стойности
print("Новият лист съдържа минималните стойности от въведените списъци:", min_values_list.remove(max_item))
