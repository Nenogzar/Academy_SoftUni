# 02_keyword_arguments_length
#################################### TASK CONDITION ############################
"""
2.	Keyword Arguments Length
Create a function called kwargs_length() that can receive some keyword arguments and return their length.
Submit only the function in the judge system.
Examples

Test Code
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

Output
2

Test Code
dictionary = {}

print(kwargs_length(**dictionary))

Output
0

"""

##########: variant 1 :##########
def kwargs_length(**kwargs):
    return len(kwargs)



##########: variant 2 :##########



