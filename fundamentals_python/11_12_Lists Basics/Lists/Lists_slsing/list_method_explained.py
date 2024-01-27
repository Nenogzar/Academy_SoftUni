people: list[str] = ['Mario', 'Ivan', 'Alexander']
print(f"{people = }")
""" 1: append """
# Index
people.append('Georgi')
print(f"people.append('Georgi') => {people = }")
"""3: copy"""
# Index
people_copy: list[str] = people.copy()
print(f"{people_copy = }")
people_copy.remove('Mario')
print(f"{people = }")
print(f"{people_copy = }")

"""4: count"""

ivan = people.count('Ivan')
print(f"count Ivan in list people = {ivan}")

"""5: extend"""
print(f"{people = }")
people1: list[str] = ['apple', 'banana']
people.extend(people1)
print(f"{people1 = }")
print(f"list people after extend list people1 {people}")

"""6: index"""
# Index
person_one = people.index('Mario')
people_two = people.index('Ivan')
print(person_one, people_two)

"""7: insert"""
# penultimate position
people.insert(-1, 'Stoyn')
print(f"{people}")

# last position
people.insert(len(people), 'Dragan')
print(f"after insert on index - len(people) {people = }")

people.insert((len(people))-2, 'Gergana')
print(f"after insert on index - (len(people))-2 {people = }")


"""8: pop"""
"""9: remove"""
"""10: reverse"""
"""11: sort"""