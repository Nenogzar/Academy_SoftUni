#################################### TASK CONDITION ############################
"""

2.	Students' Grades
Write a program that reads students' names and their grades and adds them 
to the student record. On the first line, you will receive the number of 
students – N. On the following N lines, you will be receiving a student's 
name and grade. For each student print all his/her grades and finally his/her 
average grade, formatted to the second decimal point in the format: 
"{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.

____________________________________________________________________________________________
Example_01

Input
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00	

Output
Mark -> 5.50 2.50 3.46 (avg: 3.82)
Peter -> 5.20 3.20 (avg: 4.20)
Alex -> 2.00 3.00 (avg: 2.50)

____________________________________________________________________________________________
Example_02

Input
4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.66	

Output
Ted -> 3.00 3.66 (avg: 3.33)
Scott -> 4.50 5.00 (avg: 4.75)

____________________________________________________________________________________________
Example_03

Input
5
Lee 6.00
Lee 5.50
Lee 6.00
Peter 4.40
Kenny 3.30	

Output
Peter -> 4.40 (avg: 4.40)
Lee -> 6.00 5.50 6.00 (avg: 5.83)
Kenny -> 3.30 (avg: 3.30)

"""

""" 1 """

from collections import defaultdict


class StudentsGrades:

    def __init__(self):
        self.number = int(input())
        self.students_data = defaultdict(list)
        self.message = []
        self.main()

    def add_students(self):
        for _ in range(self.number):
            name, grade = input().split()
            self.students_data[name].append(float(grade))

    def average_grade(self, data):
        return sum(data) / len(data)

    def row_of_grades(self, data):
        return ' '.join(f'{num:.2f}' for num in data)

    def main(self):
        self.add_students()
        for name, data in self.students_data.items():
            average_grade = self.average_grade(data)
            row = self.row_of_grades(data)
            self.message.append(f'{name} -> {row} (avg: {average_grade:.2f})')

    def __repr__(self):
        return '\n'.join(self.message)


if __name__ == '__main__':
    print(StudentsGrades())
