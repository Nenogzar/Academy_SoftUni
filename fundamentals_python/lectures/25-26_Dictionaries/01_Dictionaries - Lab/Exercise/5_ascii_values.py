# # Function to create a dictionary with ASCII values from a list of characters
# def create_ascii_dict(characters):
#     ascii_dict = {char: ord(char) for char in characters}
#     return ascii_dict
#
# input_characters = input().split(", ")
#
# # Creating the ASCII dictionary
# result_dict = create_ascii_dict(input_characters)
#
# # Displaying the result
# print(result_dict)

"""using comprehension """
#
# input_characters = list(map(str, input().split(", ")))
#
# ascii_dict = {char: ord(char) for char in input_characters}
#
# # Displaying the result
# print(ascii_dict)


""" """

input_string = input().split(", ")
ascii_dict = {}
for char in input_string:
    ascii_dict[char] = ord(char)
print(ascii_dict)
