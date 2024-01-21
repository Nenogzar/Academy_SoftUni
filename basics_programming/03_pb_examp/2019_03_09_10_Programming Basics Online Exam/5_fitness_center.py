trainees_number = int(input())
count_back = 0
count_chest = 0
count_legs = 0
count_abs = 0
count_ps = 0
count_pb = 0

for traine in range(trainees_number):
    type_training = input()

    if "Back" == type_training:
        count_back += 1
    elif "Chest" == type_training:
        count_chest += 1
    elif "Legs" == type_training:
        count_legs += 1
    elif"Abs" == type_training:
        count_abs += 1
    elif "Protein shake" == type_training:
        count_ps += 1
    elif "Protein bar" == type_training:
        count_pb += 1

trained = count_back + count_chest + count_legs + count_abs
purchased_product = count_pb + count_ps
purcent_traned = (trained / trainees_number) *100
purcent_purchased = (purchased_product / trainees_number) *100
print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_ps} - protein shake")
print(f"{count_pb} - protein bar")
print(f"{purcent_traned:.2f}% - work out")
print(f"{purcent_purchased:.2f}% - protein")

# jym_visitors = int(input())
#
# training_people = 0
# products = 0
#
# back = 0
# chest = 0
# legs = 0
# abs_ = 0
# shake = 0
# bar = 0
#
# for person in range(jym_visitors):
#     activity = input()
#
#     if "Protein shake" == activity or "Protein bar" == activity:
#         products += 1
#     else:
#         training_people += 1
#
#     if activity == "Back":
#         back += 1
#
#     elif activity == "Chest":
#         chest += 1
#
#     elif activity == "Legs":
#         legs += 1
#
#     elif activity == "Abs":
#         abs_ += 1
#
#     elif activity == "Protein shake":
#         shake += 1
#
#     elif activity == "Protein bar":
#         bar += 1
#
# print(f"{back} - back")
# print(f"{chest} - chest")
# print(f"{legs} - legs")
# print(f"{abs_} - abs")
# print(f"{shake} - protein shake")
# print(f"{bar} - protein bar")
# print(f"{(training_people / jym_visitors) * 100:.2f}% - work out")
# print(f"{(products / jym_visitors) * 100:.2f}% - protein")







#
#
#
# number_visitors_in_gym = int(input())
#
# gym_info = {
#     "Back": 0,
#     "Chest": 0,
#     "Legs": 0,
#     "Abs": 0,
#     "Protein shake": 0,
#     "Protein bar": 0
# }
#
# for i in range(1, number_visitors_in_gym + 1):
#     activities_in_gym = input()
#
#     gym_info[activities_in_gym] += 1
#
# work_out = gym_info["Back"] + gym_info["Chest"] + gym_info["Legs"] + gym_info["Abs"]
# protein = gym_info["Protein shake"] + gym_info["Protein bar"]
#
# work_out = (work_out / number_visitors_in_gym) * 100
# protein = (protein / number_visitors_in_gym) * 100
#
# for type_work_out, number in gym_info.items():
#     print(f"{number} - {type_work_out.lower()}")
#
# print(f"{work_out:.2f}% - work out")
# print(f"{protein:.2f}% - protein")
