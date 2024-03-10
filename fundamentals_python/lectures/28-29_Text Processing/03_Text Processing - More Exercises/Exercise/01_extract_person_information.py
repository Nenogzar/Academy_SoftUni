number_strings = int(input())

for _ in range(number_strings):
    test_string = input()
    # if all([test_string.count("@") == 1, test_string.count("|") == 1,
    #         test_string.count("#") == 1, test_string.count("*") == 1]):
    name = test_string[test_string.index("@") + 1:test_string.index("|")]
    age = test_string[test_string.index("#") + 1:test_string.index("*")]
    print(f"{name} is {age} years old.")

""" kumchovalsho """

number_of_lines = int(input())

for person in range(number_of_lines):
    current_person = input()
    name_start, name_end = current_person.index("@"), current_person.index("|")
    age_start, age_end = current_person.index("#"), current_person.index("*")
    print(f"{current_person[name_start + 1:name_end]} is {current_person[age_start + 1:age_end]} years old.")