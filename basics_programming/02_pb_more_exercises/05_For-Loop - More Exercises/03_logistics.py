load_number = int(input())
price_transport = 0
price = 0
total_tonaj = 0
low_tonaj = 0
medium_tonaj = 0
high_tonaj = 0

for ton in range(load_number):
    tonaj = int(input())

    if tonaj <= 3:
        price = tonaj * 200
        low_tonaj += tonaj
    elif tonaj <= 11:
        price = 175 * tonaj
        medium_tonaj += tonaj
    elif tonaj >= 12:
        price = 120 * tonaj
        high_tonaj += tonaj

    total_tonaj += tonaj
    price_transport += price

print(f"{price_transport / total_tonaj:.2f}")
print(f"{(low_tonaj / total_tonaj) * 100:.2f}%")
print(f"{(medium_tonaj / total_tonaj) * 100:.2f}%")
print(f"{(high_tonaj / total_tonaj) * 100:.2f}%")


# count_load = int(input())
#
# minibus = 0
# truck = 0
# train = 0
# total_load = 0
# tons = 0
# minibus_tons = 0
# truck_tons = 0
# train_tons = 0
#
# for _ in range(1, count_load + 1):
#     load = int(input())
#     tons += load
#
#     if load <= 3:
#         minibus += + load * 200
#         minibus_tons += load
#
#     elif load <= 11:
#         truck += + load * 175
#         truck_tons += load
#
#     elif load > 11:
#         train += + load * 120
#         train_tons += load
#
# total_load = minibus + truck + train
# average_per_ton = total_load / tons
# average_per_ton_minibus = (minibus_tons / tons) * 100
# average_per_ton_truck = (truck_tons / tons) * 100
# average_per_ton_train = (train_tons / tons) * 100
# print(
#     f"{average_per_ton:.2f}\n{average_per_ton_minibus:.2f}%\n{average_per_ton_truck:.2f}%\n{average_per_ton_train:.2f}%")
