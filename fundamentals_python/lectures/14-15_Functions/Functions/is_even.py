# MODULO
# In mathematics, parity refers to whether a number is either even or odd.
# The modulo % operator in programming allows one to see if two numbers divide evenly or divide andhave a remainder.
# For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenlyand would result in a number other than zero!
# In the terminal window, create a new program by typing code parity.py.
# In the text editor window, type your code as follows:

"""""""""
x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""""""""

# CREATING OUR OWN PARITY FUNCTION
# As discussed in Lecture 0, you will fi nd it useful to create a function of your own!
# We can create our own function to check whether a number is even or odd. Adjust your code as follows:

"""""""""

def main ():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return  False
main()

"""""""""
# PYTHONIC
# In the programming world, there are types of programming that are called “Pythonic” in nature.
# That is,there are ways to program that are sometimes only seen in Python programming.
# Consider the followingrevision to our program:

"""""""""
def main ():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
main()
"""""""""

# Notice that this return statement in our code is almost like a sentence in English.
# This is a unique way ofcoding only seen in Python.

# We can further revise our code and make it more and more readable:
"""""""""
def main ():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return n % 2 == 0
main()

"""""""""
# Notice that the program will evaluate what is happening within the
# n % 2 == 0
# as either true or false and simply return that to the main function.

# match
# Similar to if, elif, and else statements, match statements can be
# used to conditionally run code thatmatches certain values.
# Consider the following program:

"""""""""
name = input("What's your name? ")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""""""""
# Notice the fi rst three conditional statements print the same response.
# We can improve this code slightly with the use of the or keyword:
"""""""""
name = input("What's your name? ")
if name == name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""""""""
# Notice the number of elif statements has decreased, improving the readability of our code.
# Alternatively, we can use match statements to map names to houses. Consider the following code:
"""""""""
name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
"""""""""
# Notice the use of the _ symbol in the last case. This will match with any input,
# resulting in similar behavior as an else statement.
# A match statement compares the value following the match keyword with each
# of the values followingthe case keywords.
# In the event a match is found, the respective indented code section is executed and the program stops the matching.
# We can improve the code:

""""""""
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Drago":
        print("Slytherin")
    case _:
        print("Who?")
""""""""

#Notice, the use of the single vertical bar |
# Much like the or keyword, this allows us to check formultiple values in the same case statement.



