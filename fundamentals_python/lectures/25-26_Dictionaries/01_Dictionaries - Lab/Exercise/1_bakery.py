input_text = input().split(" ")
new_dict = {}

# for i in range(0, len(input_text), 2):
#     keys, values = input_text[i], input_text[i + 1]
#     new_dict[keys] = int(values)

new_dict = {input_text[i] : input_text[i+1] for i in range(0, len(input_text),2)}

print(new_dict)
