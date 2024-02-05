# wagon_number = int(input())
# train_wagon_index = []
#
# for _ in range(wagon_number):
#     train_wagon_index.append(0)
# # print(train_wagon_index)
#
# command_list = input().split()
#
# while command_list[0] != "End":
#
#     if command_list[0].lower() == "add":
#         train_wagon_index[-1] += int(command_list[1])
#     elif command_list[0].lower() == "insert":
#
#         train_wagon_index[int(command_list[1])] += int(command_list[2])
#     elif command_list[0].lower() == "leave":
#         train_wagon_index[int(command_list[1])] -= int(command_list[2])
#     command_list = input().split()
#
# print(train_wagon_index)


""" 2 """
train_wagons = int(input())
train = list()
command = input()

for n in range(train_wagons):
    train.append(0)


def add_people(umber_people):
    train[-1] += umber_people


def insert_people(wagon, number_people):
    train[wagon] += number_people


def leave_people(wagon, number_people):
    train[wagon] -= number_people


while command != "End":

    command = command.split()

    if "add" in command:
        add_people(int(command[-1]))

    elif "insert" in command:
        insert_people((int(command[1])), int(command[-1]))

    elif "leave" in command:
        leave_people(int(command[1]), int(command[-1]))

    command = input()

print(train)
