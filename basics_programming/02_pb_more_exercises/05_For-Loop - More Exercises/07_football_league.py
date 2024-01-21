stadium = int(input())
fen_numbers = int(input())
sec_a = 0
sec_b = 0
sec_v = 0
sec_g = 0
for _ in range(fen_numbers):
    sector = input().upper()
    if sector == "A":
        sec_a += 1
    elif sector == "B":
        sec_b += 1
    elif sector == "V":
        sec_v += 1
    elif sector == "G":
        sec_g += 1

print(f"{sec_a / fen_numbers * 100:.2f}%")
print(f"{sec_b / fen_numbers * 100:.2f}%")
print(f"{sec_v / fen_numbers * 100:.2f}%")
print(f"{sec_g / fen_numbers * 100:.2f}%")
print(f"{fen_numbers / stadium * 100:.2f}%")


# stadium_capacity = int(input())
# number_fans = int(input())
#
# a_sector = 0
# b_sector = 0
# v_sector = 0
# g_sector = 0
#
# for _ in range(1, number_fans + 1):
#     sector_type = input()
#
#     if sector_type == "A":
#         a_sector += 1
#
#     elif sector_type == "B":
#         b_sector += 1
#
#     elif sector_type == "V":
#         v_sector += 1
#
#     elif sector_type == "G":
#         g_sector += 1
#
# a_sector = (a_sector / number_fans) * 100
# b_sector = (b_sector / number_fans) * 100
# v_sector = (v_sector / number_fans) * 100
# g_sector = (g_sector / number_fans) * 100
# total_fans_on_stadium = (number_fans / stadium_capacity) * 100
#
# print(f"{a_sector:.2f}%\n{b_sector:.2f}%\n{v_sector:.2f}%\n{g_sector:.2f}%\n{total_fans_on_stadium:.2f}%")
