input_schedule = input().split(", ")
new_schedule = input_schedule.copy()


def add(lesson_tittle):
    if lesson_tittle not in new_schedule:
        new_schedule.append(lesson_tittle)


def insert(lesson_tittle, index_to_position):
    if lesson_tittle not in new_schedule:
        new_schedule.insert(index_to_position, lesson_tittle)


def remove(lesson_tittle):
    if lesson_tittle in new_schedule:
        new_schedule.remove(lesson_tittle)
    if f"{lesson_tittle}-Exercise" in new_schedule:
        new_schedule.remove(f"{lesson_tittle}-Exercise")


def swap(lesson_1, lesson_2):
    if lesson_1 in new_schedule and lesson_2 in new_schedule:
        first_lesson = new_schedule.index(lesson_1)
        second_lesson = new_schedule.index(lesson_2)
        new_schedule[first_lesson], new_schedule[second_lesson] = new_schedule[second_lesson], new_schedule[
            first_lesson]
        if lesson_2 and f"{lesson_2}-Exercise" in new_schedule:
            index_of_lesson_2 = new_schedule.index(lesson_2) + 1
            new_schedule.insert(index_of_lesson_2, f"{lesson_2}-Exercise")
            new_schedule.pop(new_schedule.index(f"{lesson_2}-Exercise", new_schedule.index(f"{lesson_2}-Exercise") + 1))
        if lesson_1 and f"{lesson_1}-Exercise" in new_schedule:
            index_of_lesson_1 = new_schedule.index(lesson_1) + 1
            new_schedule.insert(index_of_lesson_1, f"{lesson_1}-Exercise")
            new_schedule.pop(new_schedule.index(f"{lesson_1}-Exercise", new_schedule.index(f"{lesson_1}-Exercise") + 1))


def exercise(lesson_title):
    if lesson_title in new_schedule:
        if f"{lesson_title}-Exercise" not in new_schedule:
            current_lesson_index = new_schedule.index(lesson_title) + 1
            new_schedule.insert(current_lesson_index, f"{lesson_title}-Exercise")
    elif lesson_title not in new_schedule:
        new_schedule.append(lesson_title)
        new_schedule.append(f"{lesson_title}-Exercise")


command = input()
while command != "course start":
    command = command.split(":")
    operation = command[0]
    lesson_title = command[1]
    if operation == "Add":
        add(lesson_title)
    elif operation == "Insert":
        index = int(command[2])
        insert(lesson_title, index)
    elif operation == "Remove":
        remove(lesson_title)
    elif operation == "Swap":
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        swap(lesson_title_1, lesson_title_2)
    elif operation == "Exercise":
        exercise(lesson_title)
    command = input()

for count, lesson in enumerate(new_schedule, 1):
    print(f"{count}.{lesson}")


"""" 2 """

schedule_of_lessons = input().split(", ")


def check_for_exercise(find_index: int) -> bool:
    try:
        return "Exercise" in schedule_of_lessons[find_index + 1]
    except IndexError:
        return


def add_lesson(lesson_title: str) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)


def insert_lesson(lesson_title: str, index: int) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.insert(index, lesson_title)


def remove_lesson(lesson_title: str) -> None:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if check_for_exercise(find_index):
            del schedule_of_lessons[find_index]
        del schedule_of_lessons[find_index]


def swap_lesson(lesson_title: str, lesson_title_swap: str) -> None:
    if lesson_title in schedule_of_lessons and lesson_title_swap in schedule_of_lessons:
        index_lesson_one = schedule_of_lessons.index(lesson_title)
        index_lesson_two = schedule_of_lessons.index(lesson_title_swap)
        schedule_of_lessons[index_lesson_one], schedule_of_lessons[index_lesson_two] = \
            schedule_of_lessons[index_lesson_two], schedule_of_lessons[index_lesson_one]
        if check_for_exercise(index_lesson_one):
            schedule_of_lessons.insert(index_lesson_two + 1, schedule_of_lessons.pop(index_lesson_one + 1))
        if check_for_exercise(index_lesson_two):
            schedule_of_lessons.insert(index_lesson_one + 1, schedule_of_lessons.pop(index_lesson_two + 1))


def exercise_lesson(lesson_title: str) -> bool:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if not check_for_exercise(find_index):
            schedule_of_lessons.insert(find_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)
        schedule_of_lessons.append(f"{lesson_title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lesson,
    "Exercise": exercise_lesson
}

command = input()

while command != "course start":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands[command_type](*info)
    command = input()

for pos, lesson in enumerate(schedule_of_lessons, 1):
    print(f"{pos}.{lesson}")
