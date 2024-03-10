"""
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a index.
The input will be provided as a single string.
"""
from icecream import ic
input_text = input()
for index in range(len(input_text)):
    if input_text[index] != ":":
        continue
    print(input_text[index] + input_text[index + 1])

""" Ivan Shopov"""

text=input()
emoticons=[]
for char in range(0, len(text)):
    if text[char]==":":
        if char!=len(text)-1:
            print(f"{text[char]+text[char+1]}")
        else:
            break

""" CEO """

main_text = input()

for index, letter in enumerate(main_text):
    if ":" == letter:
        print(f"{letter}{main_text[index+1]}")