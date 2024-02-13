num_sp = input("Въведете числа с интервал помежу им").split()
new_list = [int(sp) for sp in num_sp]

print(new_list)
print(len(new_list))
print("[:3]", new_list[:3])
print("[1:]", new_list[1:])
print("[1:3]", new_list[1:3])
