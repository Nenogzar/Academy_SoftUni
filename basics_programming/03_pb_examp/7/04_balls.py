# number_balls = int(input())
# color_pionts = 0
#
# for color in range(number_balls):
#     collors = input().upper()
#
#     color_info ={color:
#                      {"Red": [5, 0],
#                       "Orange": [10, 0],
#                       "Yellow": [15, 0],
#                       "White": [20, 0],
#                       "Other_color": [0, 0],
#                       "Black": [0.5, 0]
#                       }
#                  }
#     for color in color_info[color]:
#         if color not in color_info:
#             color_info[color]["Other_color"][1] += 1
#             continue
#         else:
#             if color == "Black":
#                 color_pionts *= color_info[color]["Black"]
#                 color_pionts[color]["Black"][1] += 1
#             else:
#                 color_pionts *= color_info[color]
#                 color_pionts[color]["Color"][1] += 1
#
#
# print(f"Total points: {color_pionts}")
# for color in color_info:
#     print(f"{color}: {color_info[color][1]}")


#################################################
import math

number_balls = int(input())
color_points = 0
color_info = {
    "Red": [5, 0],
    "Orange": [10, 0],
    "Yellow": [15, 0],
    "White": [20, 0],
    "Black": [0.5, 0],
    "Other_color": [0, 0]
}

for _ in range(number_balls):
    color = input().capitalize()
    if color == "Black":
        color_info["Black"][1] += 1
        points = color_info["Black"][0]
        color_points = math.floor(color_points * points)
    elif color in color_info:
        color_points += color_info[color][0]
        color_info[color][1] += 1
    else:
        color_info["Other_color"][1] += 1

print(f"Total points: {color_points}")
for color in color_info:
    if color != "Black" and color != "Other_color":
        print(f"{color} balls: {color_info[color][1]}")
print(f"Other colors picked: {color_info['Other_color'][1]}")
print(f"Divides from black balls: {color_info['Black'][1]}")


