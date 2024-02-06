num_string = input().split()
even_list_str = []

for num in num_string:
    if num.lstrip('-').isdigit() and int(num) % 2 == 0:
        even_list_str.append(int(num))

print(even_list_str)


""" 2 """
num_string = input()
even_list = [int(num) for num in num_string.split() if num.lstrip('-').isdigit() and int(num) % 2 == 0]
print(even_list)



""" 3 """

def extract_even_numbers(input_string):
    even_list = []

    for num in input_string.split():
        if num.lstrip('-').isdigit() and int(num) % 2 == 0:
            even_list.append(int(num))

    return even_list

# Taking input from the user
input_numbers = input()
result = extract_even_numbers(input_numbers)
print(result)



""" 4 """

num_string = input().split()
even_list_str = [int(num) for num in filter(lambda x: (x.isdigit() or (x[0] == '-' and x[1:].isdigit())) and int(x) % 2 == 0, num_string)]
print(even_list_str)


""" 5 """
num_string = input().split()
filter_even = filter(lambda x: (x.isdigit() or (x[0] == '-' and x[1:].isdigit())) and int(x) % 2 == 0, num_string)
even_list_str = [int(num) for num in filter_even]
print(even_list_str)


""" 6 """

def filter(numbers):
    return list(s for s in numbers if s % 2 == 0)

print(filter(int(s) for s in input().split()))