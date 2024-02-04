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
