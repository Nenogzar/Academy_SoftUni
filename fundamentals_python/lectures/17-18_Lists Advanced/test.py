input_schedule = input().split(", ")
new_schedule = input_schedule.copy()

new_task = input().split(":")  # Read the first task

while new_task[0] != "course start":
    task = new_task[0]
    lesson = new_task[1]
    if new_task[-1] is enumerate:
        position_index = new_task[-1]
    else:
        position = str(new_task[-1])

    if task == 'Add':
        if lesson not in new_schedule:
            new_schedule.append(lesson)

    elif task == "Insert":
        if lesson not in new_schedule:
            if position_index is not None and position_index.isdigit():
                position_index = int(position_index)
                new_schedule.insert(position_index, lesson)
            else:
                print("Invalid index for insertion. Skipping.")

    elif task == "Remove":
        if lesson in new_schedule:
            new_schedule.remove(lesson)

    elif task == "Swap":
        if lesson in new_schedule and position in new_schedule:
            index_lesson = new_schedule.index(lesson)
            index_position = new_schedule.index(position)
            new_schedule[index_lesson], new_schedule[index_position] = new_schedule[index_position], new_schedule[index_lesson]

    elif task == "Exercise":
        # Implement the Exercise case here
        pass
    new_task = input().split(":")  # Read the next task

# print(f"{new_schedule = }")
for idx, lesson in enumerate(new_schedule, start=1):
    print(f"{idx}.{lesson}")

# Implement the exercise function if needed
# def exercise(schedule):
#    ...

# exercise(input_schedule)

