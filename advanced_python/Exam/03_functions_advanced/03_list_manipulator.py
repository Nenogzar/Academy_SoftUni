# ******* Advanced Exam - 27 June 2020 ******* #

# *******  03_list_manipulator  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2456#2

Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
•	In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
•	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
•	In case of "remove" and "beginning"
o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
o	If there are no other parameters, remove only the first element of the list.
o	Finaly, return the new list
•	In case of "remove" and "end"
o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
o	Otherwise if there are no other parameters, remove only the last element of the list.
o	Finaly, return the new list
For more clarifications, see the examples below.
Input
•	There will be no input
•	Parameters will be passed to your function
Output
•	The function should return the new list of numbers
Examples


Test Code
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))


Output
[1, 2]
[2, 3]
[20, 1, 2, 3]
[1, 2, 3, 30]
[1]
[3]
[20, 30, 40, 1, 2, 3]
[1, 2, 3, 30, 40, 50]

"""

##########: variant 1 :##########

def list_manipulator(lst, command, position, *args):
    if command == "remove":
        if position == "end":
            if args:
                for _ in range(args[0]):
                    lst.pop()
            else:
                lst.pop()
        elif position == "beginning":
            if args:
                for _ in range(args[0]):
                    lst.pop(0)
            else:
                lst.pop(0)
    elif command == "add":
        if position == "beginning":
            for number in reversed(args):
                lst.insert(0, number)
        elif position == "end":
            for number in args:
                lst.append(number)
    return lst

# Примери за използване на функцията
lst = [1,2,3]
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########


