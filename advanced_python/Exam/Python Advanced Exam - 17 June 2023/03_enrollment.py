#################################### TASK CONDITION ############################

"""
https://judge.softuni.org/Contests/Practice/Index/4081#2

03. Enrollment

You are planning to study at Software University. 
You need to choose classes so that you gather enough credits to graduate successfully.
Write a function called gather_credits that receives information about credits needed, courses, and their credits, and returns the result. The function will receive a different number of arguments. The arguments will be passed as follows:
  •	The first argument will be the number of credits you need - an integer in the range [0, 200];
  •	The following arguments will be the tuples with two elements - the first one is the course name (string), and the second one is the course credits (integer);
After receiving the information and calling the function, the program should start tracking the enrollment process:
  •	Take the course’s name from each tuple successively and if you need more credits, enroll in it, and proceed to the next one.
  •	If a course has already been enrolled in, ignore it, and proceed to the next one.
  •	If you have reached the needed number of credits, STOP enrolling!
 In the end:
  •	If you’ve managed to gather the needed credits, return the message, including the enrolled courses on a new line: 
    "Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {course1, course2, …, courseN}"
      o	return the courses’ names sorted alphabetically, in ascending order.
  •	Otherwise, return the message: 
    "You need to enroll in more courses! You have to gather {credits_shortage} credits more."

Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return one of the strings shown above depending on the result. 
Constraints
•	The first argument will always be an integer.
•	Each tuple given will always contain the course name with its credits.
Examples
Input
print(gather_credits(
    80,
    ("Basics", 27),
))

Output
You need to enroll in more courses! You have to gather 53 credits more.


Input
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

Output
Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals


Input
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

Output
Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals

"""
##########: variant 1 :##########
def gather_credits(needed_credits, *courses_info):
    gathered_credits = 0
    enrolled_courses = []

    for course_name, course_credits in courses_info:
        if gathered_credits >= needed_credits:
            break
        if course_name in enrolled_courses:
            continue
        enrolled_courses.append(course_name)
        gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        return f"""Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {', '.join(sorted(enrolled_courses))}"""
    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."

##########: variant 2 :##########


def gather_credits(needed_credits: int, *args: [str, int]):
    courses_enrolled = {}
    for course_name, course_credits in args:
        if needed_credits <= 0:
            break
        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = course_credits
            needed_credits -= course_credits

    if needed_credits <= 0:
        return (f"Enrollment finished! Maximum credits: {sum(courses_enrolled.values())}.\n"
                f"Courses: {', '.join(c for c in sorted(courses_enrolled))}")

    return f"You need to enroll in more courses! You have to gather {needed_credits} credits more."
