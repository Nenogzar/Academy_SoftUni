""" Add List Items """
#########################################################
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
#########################################################
""" Append """
# Using the append() method to append an item:

thislist.append("orange")
# output: ['apple', 'banana', 'cherry', 'orange']

thislist.append(tropical)
# output: ['apple', 'banana', 'cherry', 'orange', ["mango", "pineapple", "papaya"]]

#########################################################
""" Insert """
# The insert() method inserts an item at the specified index:

thislist.insert(1, "orange")
# output: ['apple', 'orange', 'banana', 'cherry', 'orange', ["mango", "pineapple", "papaya"]]
#########################################################
""" Extend """
#To append elements from another list to the current list, use the extend() method.

thislist.extend(tropical)
# output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
print(thislist)