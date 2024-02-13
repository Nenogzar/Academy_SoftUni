""" Loop Through a List """

thislist = ["apple", "banana", "cherry"]
#########################################################
# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

for x in thislist:
  print(x)

  #output: apple
        # banana
        # cherry
#########################################################
""" Loop Through the Index Numbers """
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

for i in range(len(thislist)):
  print(thislist[i])

  #output: apple
        # banana
        # cherry
# The iterable created in the example above is [0, 1, 2].
#########################################################
""" Using a While Loop """
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

# Print all items, using a while loop to go through all the index numbers

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  #output: apple
        # banana
        # cherry
#########################################################
""" Looping Using List Comprehension """
# A short hand for loop that will print all items in a list:

[print(x) for x in thislist]

#output: apple
        # banana
        # cherry
