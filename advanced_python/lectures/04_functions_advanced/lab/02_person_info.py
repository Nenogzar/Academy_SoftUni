
#################################### TASK CONDITION ############################
'''
https://judge.softuni.org/Contests/Practice/Index/1838#1

                        2.	Person Info
Write a function called get_info that receives a name, an age, and a town 
and returns a string in the format:

"This is {name} from {town} and he is {age} years old".

Use dictionary unpacking when testing your function. 
Submit only the function in the judge system.

_______________________________________________
Example

Test Code	(no input data in this task)

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))	

Output

This is George from Sofia and he is 20 years old

'''
##########: variant 1 :##########

def get_info(**kwargs):
    name = kwargs.get("name")
    town = kwargs.get("town")
    age = kwargs.get("age")
    return f"This is {name} from {town} and he is {age} years old"

##########: variant 2 :##########

def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))