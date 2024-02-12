# Функция за намиране на началната позиция на "k" в лабиринта
def find_position(maze):
    position = []
    for row in range(len(maze)):
        for el in maze[row]:
            if el == 'k':
                position.append(row)
                position.append(maze[row].find('k'))
                return position


# Функция за намиране на свободните позиции (' ') в лабиринта
def next_free_spot(maze):
    free_spots = []

    for row in range(len(maze)):
        for el in range(len(maze[row])):
            tmp = []
            if maze[row][el] == ' ':
                tmp.append(row)
                tmp.append(el)
                free_spots.append(tmp)

    return free_spots


# Функция за намиране на пътя в лабиринта и брой възможни изходи
def find_path(position, next_free, maze):
    total_moves = 0  # Общ брой на движенията
    total_exits = 0  # Общ брой на възможните изходи
    longest_paths = []  # Списък с най-дългите пътища

    while next_free:
        x, y = next_free.pop(0)
        moves = 0  # Брой на движенията за текущата позиция

        # Проверка за движение наляво
        if position[0] == x and position[1] - y == 1:
            moves += 1
        # Проверка за движение надясно
        elif position[0] == x and y - position[1] == 1:
            moves += 1
        # Проверка за движение надолу
        elif x - position[0] == 1 and position[1] == y:
            moves += 1
        # Проверка за движение нагоре
        elif position[0] - x == 1 and position[1] == y:
            moves += 1

        # Обновяване на броя движения за текущата позиция
        total_moves += moves

        # Проверка дали текущата позиция е изход от лабиринта
        if position[0] == 0 or position[0] == (len(maze) - 1) or position[1] == 0 or position[1] == (len(maze[0]) - 1):
            total_exits += 1

            # Запазване на текущия път
            current_path = [(position[0], position[1])] + [(x, y) for x, y in next_free]
            longest_paths.append(current_path)

    if total_exits > 0:
        # Избор на най-дългия път
        longest_path = max(longest_paths, key=len)
        return f'"Kate got out in {total_moves + 1} moves"'
    else:
        return 'Kate cannot get out'


# Вход от потребителя - брой редове в лабиринта
m_rows = int(input())
maze = []
moves = 0
free_space = True

# Вход от потребителя - редове на лабиринта
for row in range(m_rows):
    maze.append(input())

# Извикване на функциите и извеждане на резултата
position = find_position(maze)
next_free = next_free_spot(maze)
movement = find_path(position, next_free, maze)
print(movement)