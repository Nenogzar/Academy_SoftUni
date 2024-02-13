""" 1 """
input_text = input().split(" ")
wanted_palindrome = input()
palindromes = []

[palindromes.append(string) for string in input_text if string == "".join(reversed(string))]
counter_palindrom = palindromes.count(wanted_palindrome)
print(palindromes)
print(f"Found palindrome {counter_palindrom} times")

""" 2 """

input_text = input().split()
wanted_palindrome = input()

palindromes = [string for string in input_text if string == string[::-1]]
counter_palindrom = palindromes.count(wanted_palindrome)

print("Palindromes:", palindromes)
print(f"Found palindrome {counter_palindrom} times")


""" 3 """

input_text = input().split()
wanted_palindrome = input()
palindromes = []


for string in input_text:
    if string == string[::-1]:

        palindromes.append(string)
counter_palindrom = palindromes.count(wanted_palindrome)

print("Palindromes:", palindromes)
print(f"Found palindrome {counter_palindrom} times")