""" List Comprehension """
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
#########################################################
""" for loop """
#########################################################
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
#output: ['apple', 'banana', 'mango']
#########################################################
# With list comprehension you can do all that with only one line of code:

newlist1 = [x for x in fruits if "a" in x]
#output: ['apple', 'banana', 'mango']
#########################################################
""" The Syntax """
"""newlist = [expression for item in iterable if condition == True]"""
"""The return value is a new list, leaving the old list unchanged."""
#########################################################
# Example: Only accept items that are not "apple":

newlist2 = [x for x in fruits if x != "apple"]
# output: ['banana', 'cherry', 'kiwi', 'mango']

# The condition if x != "apple"  will return True for all elements other than "apple",
# making the new list contain all fruits except "apple".
#########################################################
""" With no if statement: """
#########################################################
newlist3 = [x for x in fruits] -> [newlist3.append(x) for x in fruits]
# output: ["apple", "banana", "cherry", "kiwi", "mango"]
#########################################################
""" Iterable """
#########################################################
# The iterable can be any iterable object, like a list, tuple, set etc.
# Example: You can use the range() function to create an iterable:

newlist4 = [x for x in range(10)]
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#########################################################
# Example: Accept only numbers lower than 5:

newlist5 = [x for x in range(10) if x < 5]
#output: [0, 1, 2, 3, 4]
#########################################################
# Example: Set the values in the new list to upper case:

newlist6 = [x.upper() for x in fruits]
#output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
#########################################################
# Example: Set all values in the new list to 'hello':

newlist7 = ['hello' for x in fruits]
# output: ['hello', 'hello', 'hello', 'hello', 'hello']
#########################################################
# Example: Return "orange" instead of "banana":

newlist8 = [x if x != "banana" else "orange" for x in fruits]
# output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
#########################################################
