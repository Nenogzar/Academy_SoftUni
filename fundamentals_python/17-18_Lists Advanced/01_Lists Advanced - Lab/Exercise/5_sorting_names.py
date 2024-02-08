
leter_list = list(map(str, input().split(", ")))

sorted_lst = sorted(leter_list, key=lambda x: (-len(x), x))
print(f"{sorted_lst}")
