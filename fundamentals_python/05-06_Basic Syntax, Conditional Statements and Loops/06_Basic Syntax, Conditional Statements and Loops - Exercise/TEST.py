"""
9. Sorting Hat
Help out the sorting hat to sort the new students in the houses of Hogwarts.
You will be receiving names until the command "Welcome!".
The length of each name determines in which house the student is going:

* If the name is less than 5 chars, the student is going into Gryffindor
  * Print "{name} goes to Gryffindor."
* If the name is exactly 5 chars, the student is going into Slytherin
  * Print "{name} goes to Slytherin."
* If the name is exactly 6 chars, the student is going into Ravenclaw
  * Print "{name} goes to Ravenclaw."
* If the name is more than 6 chars, the student is going into Hufflepuff
  * Print "{name} goes to Hufflepuff."

While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!
  If all students are sorted successfully, print "Welcome to Hogwarts."
"""



# voldemort_flag = False
#
# for name in iter(input, "Welcome!"):
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         voldemort_flag = True
#         break
#
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")
#
#     name = ""
#
# if not voldemort_flag:
#     print("Welcome to Hogwarts.")


# voldemort_flag = False
#
# while True:
#     name = input()
#
#     if name == "Welcome!":
#         break
#
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         voldemort_flag = True
#         break
#
#     if len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")
#
# if not voldemort_flag:
#     print("Welcome to Hogwarts.")

voldemort_flag = False
name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldemort_flag = True
        break  # Прекратява изпълнението на кода, ако се въведе "Voldemort"

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if not voldemort_flag:
    print("Welcome to Hogwarts.")

