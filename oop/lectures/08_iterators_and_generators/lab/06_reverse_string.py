def reverse_text(string):
    start_idx_str = len(string) -1
    while 0 <= start_idx_str:
        yield string[start_idx_str]
        start_idx_str -= 1



# def reverse_text(text):
#     for char in reversed(text):
#         yield char

for char in reverse_text("step"):
    print(char, end ='')



