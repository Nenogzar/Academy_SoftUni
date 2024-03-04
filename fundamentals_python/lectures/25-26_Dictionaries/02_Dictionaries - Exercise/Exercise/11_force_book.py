force_side_dict = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if ' | ' in command:
        force_side, force_user = command.split(' | ')
        present = 0
        for k, v in force_side_dict.items():
            if force_user in v:
                present = 1
        if present == 0:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                if force_user not in force_side_dict[force_side]:
                    force_side_dict[force_side].append(force_user)
    else:
        force_side, force_user = command.split(' -> ')
        present = 0
        for k, v in force_side_dict.items():
            if force_user in v:
                force_side_dict[k].pop(v.index(force_user))
                present = 1
        if present == 1:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side] += [force_user]
        else:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side] += [force_user]
        print(f"{force_user} joins the {force_side} side!")

for i in force_side_dict:
    if len(force_side_dict[i]) > 0:
        print(f"Side: {i}, Members: {len(force_side_dict[i])}")
        [print(f"! {i}") for i in (force_side_dict[i])]


""" """
#
# force_side_dict = {}
# while True:
#     command = input()
#     if command == 'Lumpawaroo':
#         break
#     if ' | ' in command:
#         command_split = command.split(' | ')
#         force_side, force_user = command_split[0], command_split[1]
#         present = 0
#         for k, v in force_side_dict.items():
#             if force_user in v:
#                 present = 1
#         if present == 0:
#             if force_side not in force_side_dict:
#                 force_side_dict[force_side] = [force_user]
#             else:
#                 if force_user not in force_side_dict[force_side]:
#                     force_side_dict[force_side].append(force_user)
#     else:
#         command_split = command.split(' -> ')
#         force_side, force_user = command_split[1], command_split[0]
#         present = 0
#         for k, v in force_side_dict.items():
#             if force_user in v:
#                 force_side_dict[k].pop(v.index(force_user))
#                 present = 1
#         if present == 1:
#             if force_side not in force_side_dict:
#                 force_side_dict[force_side] = [force_user]
#             else:
#                 force_side_dict[force_side] += [force_user]
#         else:
#             if force_side not in force_side_dict:
#                 force_side_dict[force_side] = [force_user]
#             else:
#                 force_side_dict[force_side] += [force_user]
#         print(f"{force_user} joins the {force_side} side!")
#
# for i in force_side_dict:
#     if len(force_side_dict[i]) > 0:
#         print(f"Side: {i}, Members: {len(force_side_dict[i])}")
#         [print(f"! {i}") for i in (force_side_dict[i])]