# Фаро разбъркването е метод за разбъркване на тесте карти, при което тестето се разделя точно наполовина.
# След това картите в двете половини са идеално преплетени, така че оригиналната долна карта все още е отдолу,
# а оригиналната горна карта е все още отгоре.
# Например, faro разбърква списъка
# ['ace', 'two', 'three', 'four', 'five', 'six']  веднъж, дава
# ['ace', 'four', 'two', 'five ', 'three', 'six']
# Напишете програма, която получава единичен низ (карти, разделени с интервал) и
# на втория ред получава броене на фаро разбърквания, които трябва да бъдат направени.
# Отпечатайте състоянието на тестето след разбъркването.
# Забележка: Дължината на тестето карти винаги ще бъде четно число.

input_list = input().split()
shuffles = int(input())

for _ in range(shuffles):
    middle = len(input_list) // 2
    shuffled_list = []

    for i in range(middle):
        shuffled_list.append(input_list[i])
        shuffled_list.append(input_list[i + middle])
        #  this is equal to:  shuffled_list.extend([input_list[i], input_list[i + middle]])
    input_list = shuffled_list

print(input_list)
######################## FROM CEO ##################################

# cards = input().split()
# shuffle = int(input())
# middle_of_deck = len(cards) // 2
#
# for number_of_shuffle in range(shuffle):
#     cards = [c for pair in zip(cards[:middle_of_deck], cards[middle_of_deck:]) for c in pair]
#
# print(cards)
######################## FROM CEO ##################################
#
# cards = input().split()
# shuffle = int(input())
# middle_of_deck = len(cards) // 2
#
# for number_of_shuffle in range(shuffle):
#     result_after_shuffle = []
#     for mid_card, front_card in enumerate(range(middle_of_deck), middle_of_deck):
#         result_after_shuffle.append(cards[front_card])
#         result_after_shuffle.append(cards[mid_card])
#     cards = result_after_shuffle.copy()
#
# print(cards)
######################## FROM CEO ##################################

# cards = input().split()
# shuffle = int(input())
#
# lenght = len(cards)
# mid = int(lenght / 2)
#
# for i in range(shuffle):
#     list = []
#     for p in range(0, mid):
#         list.append(cards[p])
#         list.append(cards[mid])
#         mid += 1
#     cards = list
#     mid = int(lenght / 2)
#
# print(list)
######################## FROM CEO ##################################
