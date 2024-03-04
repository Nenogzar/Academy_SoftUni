dict_courses = {}

courses_info = input()
while courses_info != "end":
    info = courses_info.split(" : ")
    if len(info) > 1:

        course_name, student_name = [item for item in info]
        if course_name not in dict_courses:
            dict_courses[course_name] = [student_name]
        else:
            if student_name not in dict_courses[course_name]:
                dict_courses[course_name].append(student_name)

    courses_info = input()

for course_name, registered_students in dict_courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
        
####################
"""whit get() method  """

dict_courses = {}

courses_info = input()
while courses_info != "end":
    courses = courses_info.split(" : ")
    course_name, student_name = courses[0], courses[1]

    dict_courses[course_name] = dict_courses.get(course_name, {})
    dict_courses[course_name][student_name] = student_name

    courses_info = input()

for key, value in dict_courses.items():
    print(f"{key}: {len(dict_courses[key])}")
    for name in dict_courses[key]:
        print(f"-- {dict_courses[key][name]}")
