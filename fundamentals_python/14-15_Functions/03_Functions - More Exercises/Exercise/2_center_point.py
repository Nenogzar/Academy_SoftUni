import math

x1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y1 = math.floor(float(input()))
y2 = math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))


def whats_closer(arg1, arg2):
    if arg1 <= arg2:
        return f"({x1}, {x2})"

    elif arg2 <= arg1:
        return f"({y1}, {y2})"


print(whats_closer(sum_x, sum_y))

""" 2 """

import math

# Function to get coordinates from the user
def get_coordinates():
    x = math.floor(float(input()))
    y = math.floor(float(input()))
    return x, y

# Function to calculate the distance from the center
def calculate_distance(coord):
    return math.floor(abs(coord[0]) + abs(coord[1]))

# Function to determine which of two points is closer to the center
def whats_closer(coord1, coord2):
    distance1 = calculate_distance(coord1)
    distance2 = calculate_distance(coord2)

    if distance1 <= distance2:
        return coord1
    else:
        return coord2

# Get coordinates for points A and B
point_a = get_coordinates()
point_b = get_coordinates()

# Determine which point is closer
closer_point = whats_closer(point_a, point_b)

print(f"{closer_point}")

