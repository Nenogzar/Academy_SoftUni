# 10_fill_the_box
#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1839#8

10.	*Fill the Box
Write a function called fill_the_box that receives a different number of arguments representing:
•	the height of a box
•	the length of a box
•	the width of a box
•	n-times a different number of cubes with exact size 1 x 1 x 1
•	a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
•	If, at the end, there is free space left in the box, print:
o	"There is free space in the box. You could put {free space in cubes} more cubes."
•	If there is no free space in the box, print:
o	"No more free space! You have {cubes left} more cubes."

Examples

Test Code
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
########################################################################
Comment:
The size of the box: 2 * 8 * 2 = 32
We put the cubes consistently. At the end there is more free space left.
########################################################################
Output
There is free space in the box. You could put 13 more cubes.

Test Code
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

########################################################################
Comment:
The size of the box: 5 * 5 * 2 = 50
We put the cubes consistently. First, we put 40 cubes and there is free space left.
Then we try to put 11 cubes, but there is only space for 10.
Cubes left: 1 + 7 + 3 + 1 + 5 = 17

########################################################################
Output
No more free space! You have 17 more cubes.

Test Code
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
Output
There is free space in the box. You could put 960 more cubes.

"""


##########: variant 1 :##########

def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    for arg in args:
        if arg == "Finish":
            break
        box_volume -= arg

    if box_volume >= 0:
        return f"There is free space in the box. You could put {box_volume} more cubes."
    else:
        return f"No more free space! You have {abs(box_volume)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

##########: variant 2 :##########


