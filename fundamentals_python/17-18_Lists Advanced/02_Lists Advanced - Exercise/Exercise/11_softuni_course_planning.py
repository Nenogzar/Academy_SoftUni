def add_lesson(schedule, lesson_title):
    """ add the lesson to the end of the schedule if it does not exist. """
    pass


def insert_lesson(schedule, lesson_title, position):
    """ insert the lesson to the given index, if it does not exist."""
    pass


def remove_lesson(schedule, lesson_title):
    """ remove the lesson, if it exists"""
    pass


def swap_lesson(schedule, command, lesson_title):
    """ swap the position of the two lessons if they exist. """
    pass


def exercise_lesson(schedule, command, lesson_title):
    """ add Exercise in the schedule right after the lesson index,
    if the lesson exists and there is no exercise already,
    in the following format "{lessonTitle}-Exercise"""
    pass


input_schedule = input().split(", ")
new_task = input().split(":")
print(f"{new_task = }")
while new_task != "course start":

    task, lesson, index = new_task[0], new_task[1], new_task[-1]
    print(f"{task = }: {lesson = }: { index = }")
    new_task = input().split(":")

    if task == 'Add':
        add_lesson(input_schedule, lesson)
    if task == "Insert":
        insert_lesson(input_schedule, lesson, index)
    if task == "Remove":
        remove_lesson(input_schedule, lesson)
    if task == "Swap":
        swap_lesson(input_schedule, lesson, index)
    if task == "Exercise"
        exercise_lesson(input_schedule, lesson)

