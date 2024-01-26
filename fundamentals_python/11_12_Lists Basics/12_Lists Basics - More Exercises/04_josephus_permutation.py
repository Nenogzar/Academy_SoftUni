# Този проблем носи името си от може би най-важното събитие в живота на древния историк Йосиф Флавий.
# Според неговата история той и неговите 40 войници са били хванати в капан в пещера от римляните по време на обсада.
# Отказвайки да се предадат на врага, те вместо това избраха масово самоубийство, с обрат:
# оформиха кръг и продължиха да убиват по един от всеки трима, докато остане един последен човек
# (и че трябваше да се самоубие, за да сложи край на акта ).
# Е, Йосиф Флавий и още един човек бяха последните и тъй като сега знаем всеки детайл от историята,
# може би правилно сте се досетили, че не са изпълнили точно първоначалната идея.
# Сега трябва да създадете програма, която отпечатва пермутация на Josephus, получавайки два реда код:
# • самия списък - числа, разделени с един интервал, представляващи хората в кръга
# • число k
# Хората стоят в кръг и чакат да бъдат екзекутирани.
# Броенето започва от първия в кръга и продължава отляво надясно.
# След като определен брой хора бъдат пропуснати, лицето k се екзекутира.
# Процедурата се повтаря с останалите хора, като се започне със следващия човек,
# върви в същата посока и се пропуска същия брой хора, докато не остане никой.
# Отпечатайте хората по ред на екзекуции във формат: "[{executed1},{executed2}, … {executedN}]"
'''
 Input                                         # Output
1 2 3 4 5 6 7
3
                                            [3,6,2,7,5,1,4]
10 5 65 104 1 0 2
8
                                            [10,65,0,1,5,2,104]


'''

input_numbers = list(map(int, input().split()))
n = len(input_numbers)

kill_step = int(input())
# Преобразуваме индекса от 1-базиран към 0-базиран
kill_step -= 1

# polovin = len(input_numbers) // 2
result, index = [], 0

while n > 0:
    index = (index + kill_step) % n
    eliminated_number = input_numbers.pop(index)
    result.append(str(eliminated_number))
    n -= 1

# even_list = result[:polovin]
# odd_list = sorted(result[polovin:])
output = "[" + ",".join(result) + "]"
print(output)
# print(even_list)
# print(odd_list)

################## whit FOR LOOP ###########################

# input_numbers = list(map(int, input().split()))
# kill_step = int(input())
# kill_step -= 1
# n = len(input_numbers)
# result, index = [], 0
#
# for _ in range(n):
#     index = (index + kill_step) % n
#     eliminated_number = input_numbers.pop(index)
#     result.append(str(eliminated_number))
#     n -= 1
#
# output = "[" + ",".join(result) + "]"
# print(output)

#################FROM SimeonChifligarov #########################

# https://github.com/SimeonChifligarov/SoftUni_Judge_Python_Problems/blob/main/Python_Fundamentals_Course/03_List_Basics_More_Exercises/04_Josephus_Permutation.py

# You are now to create a program that prints a Josephus permutation, receiving two lines of code
# the list itself (string with elements separated by a single space) and a number k)
# as if they were in a circle and counted out every k places until none remained.

# the_list_itself = [int(el) for el in input().split()]
# number_k = int(input())
# result = []
# current_list = the_list_itself.copy()
#
# for _ in range(len(the_list_itself)):
#     new_number_k = number_k
#     while new_number_k > len(current_list):
#         new_number_k -= len(current_list)
#     else:
#         result.append(current_list[new_number_k - 1])
#         current_list.pop(new_number_k - 1)
#         current_left = current_list[:new_number_k - 1]
#         current_right = current_list[new_number_k - 1:]
#         current_list = current_right + current_left
#
# result = [str(el) for el in result]
# print(f"[{','.join(result)}]")


###############################################################

# people = input().split(' ')
# k = int(input())
#
# counter = 0
# i = 0
# executed = list()
# while len(people) > 0:
#     counter += 1
#
#     if counter % k == 0:
#         # print(people[i], end=' ')
#         executed.append(people[i])
#         people.pop(i)
#     else:
#
#         i += 1
#
#     if i >= len(people):
#         i = 0
#
# prt_str = ','.join([str(x) for x in executed.copy()])
# print(f'[{prt_str}]')