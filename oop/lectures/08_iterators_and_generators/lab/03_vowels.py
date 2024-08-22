# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.all_vowers = ['a', 'e', 'i', 'o', 'u', 'y']
#         self.vowels_from_string = [el for el in self.string if el.lower() in self.all_vowers]
#         self.current_idx = -1
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         self.current_idx += 1
#         if self.current_idx < len(self.vowels_from_string):
#             return self.vowels_from_string[self.current_idx]
#         raise StopIteration


class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = 'aeiouAEIOU'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if char in self.vowels:
                return char
        raise StopIteration


my_string = vowels('Abcedifuty0o')

for char in my_string:

    print(char)
