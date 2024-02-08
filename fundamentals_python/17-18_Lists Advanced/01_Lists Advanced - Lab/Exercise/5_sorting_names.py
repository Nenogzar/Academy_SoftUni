leter_list = list(map(str, input().split(", ")))

sorted_lst = sorted(leter_list, key=len, reverse=True)
print(f"{sorted_lst}")


"""  whit lambda """

leter_list = list(map(str, input().split(", ")))

sorted_lst = sorted(leter_list, key=lambda x: len(x), reverse=True)
print(f"{sorted_lst = }")


