""" add 1 to any elements in dict """
def add_one(x):
    return x + 1
d = {'a':1, 'b':2, 'c':3}

result = map(add_one, d.values())
print(list(result))

######################################
""" list """
list1 = ["I", "Logical"]
list2 = ["Love", "Python"]
new = []
for i in range(len(list1)):
    new.append(list1[i]+" "+list2[i])
print(" ".join(new))

""" doctionary """
dict1 = {"first": "I", "second": "Logical"}
dict2 = {"first": "Love", "second": "Python"}
new_dict = {}

for key in dict1:
    new_dict[key] = dict1[key] + " " + dict2[key]
print(f"{new_dict = }")
result = " ".join(new_dict.values())
print(result)
######################################

