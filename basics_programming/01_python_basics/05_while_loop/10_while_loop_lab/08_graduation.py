student_name = input()
counter_grades = 0
year_counter = 0
year_failed = 0

while year_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4.00:
        year_failed += 1
        if year_failed >1:
            excluded_year =year_counter +1
            print(f"{student_name} has been excluded at {excluded_year} grade")
            break

        continue
    year_counter += 1
    counter_grades += annual_grade

else:
    average_grade = counter_grades / year_counter
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
