input_string = list(map(int, input().split(", ")))
print(input_string)
for num in input_string:
    num_str = str(num)
    if num_str == num_str[::-1]:
        command = "True"
    else:
        command = "False"

    print(command)

""" 2 """

input_string = list(map(int, input().split(", ")))
result = ["True" if str(num) == str(num)[::-1] else "False" for num in input_string]
print("\n".join(result))

""" 3 """


def palindrom_func(input):
    results = []
    for num in input:
        num_str = str(num)
        if num_str == num_str[::-1]:
            results.append("True")
        else:
            results.append("False")
    return results


inp_string = list(map(int, input().split(", ")))
palindrom = palindrom_func(inp_string)
print("\n".join(palindrom))

""" 4 """


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def palindrome_function(lst):
    return '\n'.join(['True' if is_palindrome(num) else 'False' for num in lst])


list_of_palindromes = list(map(int, input().split(', ')))
print(palindrome_function(list_of_palindromes))

""" 5 """


def check_palindrome(numbers):
    [print(n == n[::-1]) for n in numbers]


check_palindrome(input().split(", "))
