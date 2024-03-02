command = input().split(":")
student_dict = {}

while len(command) > 1:

    studen, id_student, course  = command
    student_dict[studen] = (id_student, course)
    command = input().split(":")
#print(student_dict)
# {'Peter': ('123', 'programming basics'), 'John': ('5622', 'fundamentals'), 'Maya': ('89', 'fundamentals'), 'Lilly': ('633', 'fundamentals')}
value = command[0]
formatted_value = value.replace('_', ' ')

for name, (id, courses) in student_dict.items():
    if formatted_value == courses:
        print(f"{name} - {id}")

#
#
# """kumchovylcho solution"""
#
# courses = dict()
#
# fill_in_students = input()
# while ":" in fill_in_students:
#     fill_in_students = fill_in_students.split(":")
#
#     student_course = fill_in_students[2]
#     student_ID = fill_in_students[1]
#     student_name = fill_in_students[0]
#
#     if student_course not in courses:
#         courses[student_course] = dict()
#
#     courses[student_course][student_name] = student_ID
#     fill_in_students = input()
#
# fill_in_students = fill_in_students.replace("_", " ")
#
# if fill_in_students in courses:
#     for id in courses[fill_in_students]:
#         print(f"{id} - {courses[fill_in_students][id]}")

"""CEO solution """

# student_information = input()
# student_dic = {}
#
# while not student_dic.get(student_information):
#     student_information = student_information.split(":")
#     name_student, id_student, couse_student = student_information
#
#     if couse_student not in student_dic:
#         student_dic[couse_student] = {}
#     student_dic[couse_student][name_student] = id_student
# #   {'programming basics': {'Peter': '123'}, 'fundamentals': {'John': '5622', 'Maya': '89', 'Lilly': '633'}}
#     student_information = input()
#
#     student_information = student_information.replace("_", " ")
#
# for key, value in student_dic[student_information].items():
#     print(f"{key} - {value}")