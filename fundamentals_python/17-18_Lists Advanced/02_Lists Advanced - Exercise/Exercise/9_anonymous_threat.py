main_string = input().split()
commands = input()


while commands != "3:1":
    # Разделяме командата и индексите и ги конвертирам към нужния тип данни
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in commands.split()]

    if command == "merge":
        # Проверка за невалиден стартов индекс и корекция ако е необходимо
        if start_index < 0:
            start_index = 0
        # Проверка за валидност на интервала
        if start_index < end_index:
            how_long = len(main_string)
            # Корекция на краен индекс, ако е извън границите на списъка
            if end_index >= how_long:
                end_index = how_long - 1
            # Обхождаме интервала и сливаме съседни елементи
            for num in range(start_index, end_index):
                main_string[start_index] += f"{main_string.pop(start_index + 1)}"

    elif command == "divide":
        index_ = start_index
        partitions = end_index
        # Проверка за валиден стартов индекс
        if 0 <= index_ < len(main_string):
            how_long = len(main_string[index_])
            space_between = how_long // partitions
            string_to_change = main_string.pop(index_)
            result_ = []
            # Разделяме думата на равни части
            for x in range(partitions - 1):
                result_.append(string_to_change[:space_between])
                string_to_change = string_to_change[space_between:]
            result_.append(string_to_change)
            # Вмъкваме новите части в основния списък
            for x in result_[::-1]:
                main_string.insert(index_, x)


    commands = input()


print(" ".join(main_string))

""" 2 """
words = input().split()


def merge(start_index, end_index, words):
    current_merge = []
    all_in_one_string = ""
    if start_index < 0:
        start_index = 0
    elif start_index > len(words):
        start_index = len(words) - 2
    if end_index > len(words):
        end_index = len(words) - 1
    current_merge += words[start_index:end_index + 1]
    for word in current_merge:
        all_in_one_string += word
    del words[start_index:end_index + 1]
    words.insert(start_index, all_in_one_string)


def divide(divide_index, how_many_pieces, words):
    how_long = len(words[divide_index])
    space_between = how_long // how_many_pieces
    string_to_change = words.pop(divide_index)
    result_ = []
    for x in range(how_many_pieces - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        words.insert(divide_index, x)


command = input()
while command != "3:1":
    command = command.split()
    operation = command[0]
    if operation == "merge":
        merge(int(command[1]), int(command[2]), words)
    elif operation == "divide":
        divide(int(command[1]), int(command[2]), words)
    command = input()

print(*words)


"""  3 Bilyana Panova"""


def valid_index(start, end):
    if start < 0:
        start = 0
    if end >= len(strings):
        end = len(strings) - 1
    return start, end


strings = input().split()
commands = input()
while commands != "3:1":
    command = commands.split()
    if command[0] == "merge":
        start_index, end_index = valid_index(int(command[1]), int(command[2]))
        strings[start_index:end_index + 1] = ["".join(strings[start_index:end_index + 1])]
    elif command[0] == "divide":
        index, partitions = int(command[1]), int(command[2])
        cut_part = len(strings[index]) // partitions
        text = strings.pop(index)
        counter = 1
        while True:
            if counter < partitions:
                strings.insert(index, text[:cut_part])
                text = (text[cut_part:])

            else:
                strings.insert(index, text)
                break
            index += 1
            counter += 1
    commands = input()
else:
    print(" ".join(strings))