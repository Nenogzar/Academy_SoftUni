def remove_vowels(text):
    # Create a list of vowels to be removed
    vowels = ['a', 'o', 'u', 'e', 'i']

    new_text = [char for char in text if char.lower() not in vowels]

    return ''.join(new_text)


input_string = input()

print(remove_vowels(input_string))
