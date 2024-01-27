""" Remove List Items """

thislist = ["apple", "banana", "cherry"]
#########################################################
""" remove """
# The remove() method removes the specified item.
# If there are more than one item with the specified value, the remove() method removes the first occurance

thislist.remove("banana")
# output: ['apple', 'cherry']
#########################################################
""" Remove Specified Index """
#########################################################
""" pop() """
# The pop() method removes the specified index.

thislist.pop(1)
# output: ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
# Remove the last item:

thislist.pop()
# output: ['apple', 'banana']
#########################################################
""" del """
# The del keyword also removes the specified index:

del thislist[0]
# output: ['banana', 'cherry']

# The del keyword can also delete the list completely.
del thislist
# print(thislist) -> this will cause an error because you have succsesfully deleted "thislist".

#########################################################
""" Clear the List """
#########################################################
""" clear() """

thislist.clear()
#output: []
