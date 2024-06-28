#################################### TASK CONDITION ############################
'''
https://judge.softuni.org/Contests/Practice/Index/1934#0
                   1.	Rhombus of Stars
Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

____________________________________________________________________________________________
Example_01

Input
1

Output
*

____________________________________________________________________________________________
Example_02

Input
2

Output
 *
* *
 *

____________________________________________________________________________________________
Example_03

Input
3
  *
 * *
* * *
 * *
  *

____________________________________________________________________________________________
Example_04

Input
4

Output
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

'''
##########: variant 1 :##########

n = int(input())


def print_row(size, row):
    empty = " "
    star = "* "
    print(f"{empty *(size-row)}{star * row}")


def print_upper_part(size):
    for row in range(1, size + 1):
        print_row(size, row)


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhumbus(size):
    print_upper_part(size)
    print_bottom_part(size)


print_rhumbus(n)

"""  OR 
# 3 parts:  
# upper, center, bottom

n = int(input())


def print_row(size, row):
    empty = " "
    star = "* "
    print(f"{empty * (size - row)}{star * row}")


def print_upper_part(size):
    for row in range(1, size):
        print_row(size, row)


def print_center_part(size):
    print_row(size, size)


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhumbus(size):
    print_upper_part(size)
    print_center_part(size)
    print_bottom_part(size)


print_rhumbus(n)

"""



# ##########: variant 2 :##########
#
# def print_row(size_of_rhombus, stars):
#     for row in range(size_of_rhombus - stars):
#         print(" ", end="")
#     for row in range(1, stars):
#         print("*", end=" ")
#     print("*")
#
#
# size = int(input())
# for star_count in range(1, size):
#     print_row(size, star_count)
# for star_count in range(size, 0, -1):
#     print_row(size, star_count)
#
# # ##########: variant 3 Class :##########
#
#
# number_of_rhombus = int(input())
#
#
# class Rhombus:
#     def __init__(self, stars):
#         self.stars = stars
#         self.draw = []
#
#     def make_rhombus(self):
#         for row in range(1, self.stars + 1):
#             if row == 1:
#                 self.draw.append((self.stars - row) * " " + row * "*")
#             else:
#                 self.draw.append((self.stars - row) * " " + row * "* ")
#         for rows in range(0, self.stars - 1):
#             if rows == 0:
#                 self.draw.append((self.stars - (row - 1)) * " " + (self.stars - 1) * "* ")
#             else:
#                 self.draw.append((rows + 1) * " " + (self.stars - rows - 1) * "* ")
#
#     def __repr__(self):
#         return '\n'.join(self.draw)
#
#
# r = Rhombus(number_of_rhombus)
# r.make_rhombus()
# print(r)
#
#
# ##########: variant 4 whit Class :##########
#
# class Size:
#
#     def __init__(self):
#         self.size = int(input())
#
#
# class Rhombus:
#
#     def __init__(self):
#         self.storage = []
#
#     def generate_figure(self, size):
#         for num in range(1, size * 2):
#             row = self.spaces(num, size) + self.stars(num, size)
#             self.storage.append(row)
#
#     @staticmethod
#     def spaces(number, size) -> str:
#         return ' ' * abs(number - size)
#
#     @staticmethod
#     def stars(number, size) -> str:
#         return '* ' * (size - (abs(number - size)))
#
#
# class Draw:
#
#     def __init__(self, data):
#         self.data = data
#
#     def draw_image(self):
#         for row in self.data.storage:
#             print(row)
#
#
# if __name__ == '__main__':
#     size = Size()
#     rhombus = Rhombus()
#     rhombus.generate_figure(size.size)
#     result = Draw(rhombus)
#     result.draw_image()
