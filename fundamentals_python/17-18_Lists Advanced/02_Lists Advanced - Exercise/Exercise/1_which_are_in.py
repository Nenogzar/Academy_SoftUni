"""1 """
list_one = input().split(", ")
list_two = input().split(", ")

result_list = list()

for n in list_one:
    for i in list_two:
        if n in i:
            result_list.append(n)
result_list = list(dict.fromkeys(result_list))
print(result_list)

""" 2 """

words = input().split(", ")
check_if_words_are_in = input().split(", ")
list_with_checked_words = []


def which_are_in(string, check_strings):
    for word in string:
        for check_word in check_strings:
            if word in check_word:
                list_with_checked_words.append(word)
                break
    return list_with_checked_words


print(which_are_in(words, check_if_words_are_in))

""" 3 """

list_one, list_two = input().split(", "), input().split(", ")

result_list = list()
[result_list.append(n) for n in list_one for i in list_two if n in i]
result_list = list(dict.fromkeys(result_list))
print(result_list)
