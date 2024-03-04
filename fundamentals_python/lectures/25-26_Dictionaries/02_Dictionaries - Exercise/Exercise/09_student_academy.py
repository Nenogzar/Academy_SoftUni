""" whit list for grades"""
students = {}
student_number = int(input())

for _ in range(student_number):
    name, grade = input(), float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        # students[name] = {"grades": grades, "average_grade": average_grade}
        print(f"{name} -> {average_grade:.2f}")
# print(students)

""" whit nested dict for grades"""

number_students = int(input())

students_grades = {}

for _ in range(number_students):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = {}
        students_grades[name][name + str(grade)] = 0
    if name in students_grades:
        students_grades[name][name + str(grade)] = 0
    students_grades[name][name + str(grade)] += grade

for name_student in students_grades:
    score = 0
    for key, value in students_grades[name_student].items():
        score += value
    average_score = score / len(students_grades[name_student])
    if average_score >= 4.50:
        print(f"{name_student} -> {average_score:.2f}")
print(students_grades)

""" whit list for grades"""

students_with_grades = dict()


def main():
    pair_of_rows = int(input())
    for pair in range(pair_of_rows):
        student_name = input()
        student_grade = float(input())

        if student_name not in students_with_grades:
            students_with_grades[student_name] = []

        students_with_grades[student_name].append(student_grade)

    average_grade_checker()


def average_grade_checker():
    for student in students_with_grades:
        average_grade = sum(students_with_grades[student]) / len(students_with_grades[student])
        if average_grade >= 4.50:
            print(f"{student} -> {average_grade:.2f}")
    print(students_with_grades)
main()