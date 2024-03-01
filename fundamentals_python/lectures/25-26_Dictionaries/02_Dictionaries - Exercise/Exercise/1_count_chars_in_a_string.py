def count_letter(current_text):
    char_dict = {}

    for word in current_text:
        for letter in word:
            if letter not in char_dict:
                char_dict[letter] = 1
            else:
                char_dict[letter] += 1
    return char_dict



input_str = input().split(" ")
char_dict = count_letter(input_str)

for k, v, in char_dict.items():
    print(f"{k} -> {v}")