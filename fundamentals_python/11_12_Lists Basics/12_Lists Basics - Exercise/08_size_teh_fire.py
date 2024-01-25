# Създайте програма, която изчислява водата, необходима за гасене на „пожарна клетка“,
# въз основа на предоставената информация за нейното „ниво на пожар“ и колко е засегната от водата.
# Първо ще ви бъде дадено нивото на пожар вътре в клетката с целочислената стойност на клетката,
# което представлява необходимата вода за гасенето на огъня. Те ще бъдат дадени в следния формат:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# След това ще получите количеството вода, което имате за гасене на пожарите.
# Има диапазон на пожар за всеки тип пожар и ако стойността на клетка е под или надвишава нея,
# тя е невалидна и не е необходимо да я гасите.

# Тип пожарен диапазон
# High      81 - 125
# Medium    51 - 80
# Low        1 - 50

# Ако една клетка е валидна, трябва да я изгасите, като намалите водата с нейната стойност.
# Гасенето на пожар също изисква усилия и трябва да ги пресметнете.
# Стойността му е равна на 25% от стойността на клетката.
# В крайна сметка ще трябва да отпечатате общото усилие.
# Продължете да пускате клетки, докато не ви свърши водата.
# Пропуснете го и опитайте следващия, ако нямате достатъчно вода,
# за да изгасите дадена клетка.
# Накрая отпечатайте клетките, които сте поставили в следния формат:
# „Cells:
#   - {ceill1}
#   - {ceill2}
#   …
#   - {cellN}"
# „Effort: {effort}“
# Усилието трябва да бъде форматирано до втория знак след десетичната запетая.
# Накрая отпечатайте общия пожар, който сте потушили от всички клетки в следния формат:
# "Total Fire: {total_fire}"
# Вход / Ограничения
# • На 1-ви ред ще получите пожарите с техните клетки в описания по-горе формат – цели числа в диапазона [1…500].
# • На 2-ри ред ще получите водата – цяло число в диапазона [0….100000].
# Изход
# Отпечатайте резултата, както е описано по-горе.
# След като прочетем изхода, започваме да проверяваме нивото на пожара и неговата валидност.
# Първото е валидно, така че изваждаме 89 от количеството вода – 1250 и водата става 1161.
# Трябва да изчислим усилието, което е 25% от 89.
# Ще добавим 89 към общия пожар, който сме потушили .
# В крайна сметка усилието е 54,22, а общият огън: 217

fire_input = input().split("#")
water = int(input())
total_fire, effort = 0, 0

print("Cells:")
for element in fire_input:
    element_value = int(element.split("= ")[1])
    if water >= element_value:
        if element.startswith("High") and element_value in range(81, 126):
            water -= element_value
            total_fire += element_value
            print(f" - {element_value}")

        elif element.startswith("Medium") and element_value in range(51, 81):
            water -= element_value
            total_fire += element_value
            print(f" - {element_value}")

        elif element.startswith("Low") and element_value in range(1, 51):
            water -= element_value
            total_fire += element_value
            print(f" - {element_value}")


    effort = total_fire * 0.25

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

########################## FROM CEO ########################

# fire_levels = input().split("#")
# water = int(input())
#
# put_out_cells = list()
# effort, total_fire, water_left = 0, 0, water
#
# for clean_text in fire_levels:
#     type_of_fire, cell_value = [int(x) if x.isdigit() else x for x in clean_text.split(" = ")]
#     if water_left >= cell_value:
#         if any(["High" in type_of_fire and cell_value in range(81, 126),
#                 "Low" in type_of_fire and cell_value in range(1, 51),
#                 "Medium" in type_of_fire and cell_value in range(51, 81)]):
#             put_out_cells.append(cell_value)
#             effort += cell_value * 0.25
#             total_fire += cell_value
#             water_left -= cell_value
#
# print("Cells:")
# for n in put_out_cells:
#     print(f" - {n}")
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")


################################### OTHER Short ###############################################

# fire_input = input().split("#")
# water = int(input())
# total_fire, effort = 0, 0
#
# print("Cells:")
# for element in fire_input:
#     element_value = int(element.split("= ")[1])
#
#     if water >= element_value and any(element.startswith(fire_type)
#                                       and min_range <= element_value <= max_range
#                                       for fire_type, min_range, max_range
#                                       in [("High", 81, 125), ("Medium", 51, 80), ("Low", 1, 50)]):
#         water -= element_value
#         total_fire += element_value
#         print(f" - {element_value}")
#
# effort = total_fire * 0.25
#
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")


