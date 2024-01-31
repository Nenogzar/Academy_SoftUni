width  = int(input())
height = int(input())
def rectangle_area(width, height):
    area = width * height
    return area

print(rectangle_area(width, height))


#

a, b = int(input()), int(input())
area_calculation = lambda side_a, side_b: side_a * side_b
print(area_calculation(a, b))