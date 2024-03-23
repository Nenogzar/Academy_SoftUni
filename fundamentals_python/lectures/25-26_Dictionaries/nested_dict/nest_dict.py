def student_marks(courses):
    marks_dict = {}
    name = input("Enter your name: ")
    marks_dict[name] = {}
    for course in courses:
        mark = int(input(f"Enter your {course}'s marks: "))
        marks_dict[name][course] = mark
    marks_dict[name]['logic'] = int(input("Enter your logic: "))
    return marks_dict

student1 = ['python', 'stats', 'database']
print(student_marks(student1))
