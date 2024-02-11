def add_lesson(schedule, lesson_title):
    pass


def insert_lesson(schedule, lesson_title):
    pass

def remove_lesson(schedule, lesson_title):
    pass

def swap_lesson(schedule, command, lesson_title):
    pass


def exercise_lesson(schedule, command, lesson_title):
    pass


#input_schedule = input().split(", ")
new_task = input().split(":")
print(f"{new_task = }")
while new_task != "course start":

    task, lesson, index = new_task[0], new_task[1], new_task[-1]
    print(f"{task = }{lesson = }{ index = }")
    new_task = input().split(":")

if task == 'Add'
    add_lesson()


