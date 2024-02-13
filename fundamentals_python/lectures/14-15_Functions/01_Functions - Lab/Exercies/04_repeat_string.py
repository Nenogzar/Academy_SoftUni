# whit list
string_input = input()
repeat_range = int(input())
new_string = []

for _ in range(repeat_range):
    new_string.append(string_input)

result_string = ''.join(new_string)
print(result_string)


# or whit Function

def repeat_string(input_string, repeat_range):
    new_string = []

    for _ in range(repeat_range):
        new_string.append(input_string)

    result_string = ''.join(new_string)
    return result_string


string_input = input()
repeat_range = int(input())

result = repeat_string(string_input, repeat_range)
print(result)

# whit string

string_input = input()
repeat_range = int(input())


def repeat_string(string_input, repeat_range):
    result_string = ''

    for _ in range(repeat_range):
        result_string += string_input

    return result_string


#  kumchovylcho

text = input()
times_to_copy = int(input())


def new_text(string, times_multiplied):
    result = string * times_multiplied
    return result


print(new_text(text, times_to_copy))
