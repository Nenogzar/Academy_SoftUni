""" List Methods """

list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
list3 = []

# Python has a set of built-in methods that you can use on lists.
# Method	      #              Description                    #
#################################################################
# append()	        Adds an element at the end of the list
list3.append("e")
""" ['e'] """
list3.append((list2))
""" ['e', ['a', 'b', 'c', 'd']] """
#################################################################
# insert()	        Adds an element at the specified position   #
list3.insert(2, "f")
""" ['e', ['a', 'b', 'c', 'd'], 'f'] """
#################################################################
# len()                                                         #
len(list3)
""" 3 """
#################################################################
# clear()	        Removes all the elements from the list      #
list3.clear()
""" [] """
#################################################################
# copy()	        Returns a copy of the list                  #
list3 = list2.copy()
""" ['a', 'b', 'c', 'd'] """
#################################################################
# index()	        Returns the index of the first element with the specified value
list3.index("b")
""" 1 """
#################################################################
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
alfa = "a"
list3.extend(alfa)
""" ['a', 'b', 'c', 'd', 'a'] """
#################################################################
# count()	        Returns the number of elements with the specified value
list3.count("a")
""" 2 """
#################################################################
# pop()	            Removes the element at the specified position
list3.pop(3)
""" ['a', 'b', 'c', 'a'] """
#################################################################
# remove()	        Removes the item with the specified value - first of them
list3.remove("a")
""" ['b', 'c', 'a'] """
#################################################################
# sort()	        Sorts the list                              #
list3.sort()
"""['a', 'b', 'c']"""
#################################################################
# reverse()	        Reverses the order of the list              #
list3.reverse()
""" ['c', 'b', 'a']"""
