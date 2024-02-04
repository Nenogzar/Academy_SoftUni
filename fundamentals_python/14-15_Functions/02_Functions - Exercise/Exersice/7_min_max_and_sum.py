list_number = list(map(int, input().split(" ")))
minimum_number = min(list_number)
maximum_number = max(list_number)
sum_of_all_numbers = sum(list_number)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")

""" 2 """

def analyze_numbers(numbers):
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    sum_of_all_numbers = sum(numbers)

    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_all_numbers}")

# Example usage:
list_number = list(map(int, input().split()))
analyze_numbers(list_number)

""" 3 """
numbers = list(map(int, input().split()))
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum of all numbers is: {sum(numbers)}")
