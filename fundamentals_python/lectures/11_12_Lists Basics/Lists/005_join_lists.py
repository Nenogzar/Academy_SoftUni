""" Join Two Lists """

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
##############################################################################
# One of the easiest ways are by using the + operator.

list1 = list1 + list2
"""['a', 'b', 'c', 1, 2, 3]"""
list1 = list1[:3]
##############################################################################
# Another way to join two lists is by appending all the items from list2 into list1, one by one:
# Example
# Append list2 into list1:

for x in list2:
  list1.append(x)
"""['a', 'b', 'c', 1, 2, 3]"""
list1 = list1[:3]
##############################################################################
# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:

list1.extend(list2)
"""['a', 'b', 'c', 1, 2, 3]"""
