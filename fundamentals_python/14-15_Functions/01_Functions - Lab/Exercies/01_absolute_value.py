main_list = [float(num) for num in input().split()]

def abs_value(main_list):
    result = [abs(lement) for lement in main_list]
    return print(result)

abs_value(main_list)