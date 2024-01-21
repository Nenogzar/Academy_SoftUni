season = input()
group_type = input()
number_students = int(input())
number_sleeps = int(input())

sport = ''
price = 0
discount = 1

if group_type in 'boys, girls':

    if season == 'Winter':
        price = 9.60

    elif season == 'Spring':
        price = 7.20

    elif season == 'Summer':
        price = 15

elif group_type == 'mixed':

    if season == 'Winter':
        price = 10

    elif season == 'Spring':
        price = 9.50

    elif season == 'Summer':
        price = 20

if number_students >= 50:
    discount = 0.50

elif number_students >= 20:
    discount = 0.85

elif number_students >= 10:
    discount = 0.95

total_sum = ((number_students * price) * number_sleeps) * discount

if group_type == 'girls':

    if season == 'Winter':
        sport = 'Gymnastics'

    elif season == 'Spring':
        sport = 'Athletics'

    elif season == 'Summer':
        sport = 'Volleyball'

elif group_type == 'boys':

    if season == 'Winter':
        sport = 'Judo'

    elif season == 'Spring':
        sport = 'Tennis'

    elif season == 'Summer':
        sport = 'Football'

elif group_type == 'mixed':

    if season == 'Winter':
        sport = 'Ski'

    elif season == 'Spring':
        sport = 'Cycling'

    elif season == 'Summer':
        sport = 'Swimming'

print(f'{sport} {total_sum:.2f} lv.')








# season = input()
# group_type = input()
# number_studens = int(input())
# number_sleeps = int(input())
#
# vacantion_info = {
#     "Winter": {
#         "boys": "Judo",
#         "girls": "Gymnastics",
#         "mixed": "Ski"},
#     "Spring": {
#         "boys": "Tennis",
#         "girls": "Athletics",
#         "mixed": "Cycling"},
#     "Summer": {
#         "boys": "Football",
#         "girls": "Volleyball",
#         "mixed": "Swimming"},
#     "price": {
#         "Winter": [9.60, 10],
#         "Spring": [7.20, 9.5],
#         "Summer": [15, 20]}}
#
# discount = 1
# if 10 <= number_studens < 20:
#     discount = 0.95
# elif 20 <= number_studens < 50:
#     discount = 0.85
# elif number_studens >= 50:
#     discount = 0.50
#
# total_price = ((vacantion_info["price"][season][
#                     0 if group_type != "mixed" else 1] * number_sleeps) * number_studens) * discount
# print(f"{vacantion_info[season][group_type]} {total_price:.2f} lv.")


# whit function and list
# def calculate_discount(student_number):
#     if 10 <= student_number < 20:
#         return 0.95
#     elif 20 <= student_number < 50:
#         return 0.85
#     elif student_number >= 50:
#         return 0.5
#     else:
#         return 1
#
# def main():
#     season = input()
#     group_type = input()
#     student_number = int(input())
#     nights_number = int(input())
#
#     night_price = 0.0
#     sports = ""
#     discount = calculate_discount(student_number)
#
#     if season == "Winter":
#         if group_type == "boys":
#             night_price = 9.60
#             sports = "Judo"
#         elif group_type == "girls":
#             night_price = 9.60
#             sports = "Gymnastics"
#         elif group_type == "mixed":
#             night_price = 10
#             sports = "Ski"
#     elif season == "Spring":
#         if group_type == "boys":
#             night_price = 7.20
#             sports = "Tennis"
#         elif group_type == "girls":
#             night_price = 7.20
#             sports = "Athletics"
#         elif group_type == "mixed":
#             night_price = 9.5
#             sports = "Cycling"
#     elif season == "Summer":
#         if group_type == "boys":
#             night_price = 15
#             sports = "Football"
#         elif group_type == "girls":
#             night_price = 15
#             sports = "Volleyball"
#         elif group_type == "mixed":
#             night_price = 20
#             sports = "Swimming"
#
#
#
#     price = (student_number * nights_number) * night_price
#     price_discount = price * discount
#
#     if student_number > 0 and nights_number > 0:
#         print(f"{sports} {price_discount:.2f} lv.")
#
# if __name__ == "__main__":
#     main()
